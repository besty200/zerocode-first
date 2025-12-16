
import pygame
import random

# Инициализация библиотеки pygame
pygame.init()

# Определение размеров окна игры
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# Размер клетки змейки и еды
CELL_SIZE = 20

# Расчет количества клеток по горизонтали и вертикали
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Цвета в формате RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создаем окно игры
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Змейка")

# Создаем объект для отслеживания времени
clock = pygame.time.Clock()

# Определение направлений движения змейки
directions = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0)
}

class Snake:
    """
    Класс, представляющий змейку.
    """
    def __init__(self):
        # Начальная позиция змейки: в центре экрана
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        # Начальное направление движения
        self.direction = 'RIGHT'
        # Флаг, указывающий, есть ли змейка на экране
        self.grow = False

    def get_head_position(self):
        """
        Возвращает текущую позицию головы змейки.
        """
        return self.positions[0]

    def turn(self, direction):
        """
        Изменяет направление движения змейки.
        Предотвращает возможность разворота на 180 градусов.
        """
        opposite_directions = {'UP':'DOWN', 'DOWN':'UP', 'LEFT':'RIGHT', 'RIGHT':'LEFT'}
        if direction != opposite_directions[self.direction]:
            self.direction = direction

    def move(self):
        """
        Выполняет перемещение змейки в текущем направлении.
        Завершает игру, если змейка выходит за границы или врезается в себя.
        """
        current = self.get_head_position()
        move_x, move_y = directions[self.direction]
        new_x = current[0] + move_x
        new_y = current[1] + move_y
        new_position = (new_x, new_y)

        # Проверка выхода за границы
        if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0 or new_y >= GRID_HEIGHT:
            raise Exception('Game Over: Змейка вышла за границы поля')

        # Проверка столкновения с самим собой
        if new_position in self.positions[1:]:
            raise Exception('Game Over: Змейка столкнулась сама с собой')

        # Обновление позиции
        self.positions = [new_position] + self.positions
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False

    def grow_snake(self):
        """
        Указывает змейке расти при следующем движении.
        """
        self.grow = True

    def draw(self, surface):
        """
        Отрисовка змейки на поверхности.
        """
        for position in self.positions:
            rect = pygame.Rect(position[0] * CELL_SIZE, position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

class Food:
    """
    Класс, представляющий еду.
    """
    def __init__(self, snake_positions):
        self.position = self.random_position(snake_positions)

    def random_position(self, snake_positions):
        """
        Генерирует случайную позицию еды, которая не занимает змейка.
        """
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_positions:
                return pos

    def draw(self, surface):
        """
        Отрисовка еды на поверхности.
        """
        rect = pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, RED, rect)

def main():
    """
    Основная функция запуска игры.
    """
    snake = Snake()
    food = Food(snake.positions)
    score = 0
    font = pygame.font.SysFont("Arial", 24)

    running = True
    while running:
        clock.tick(10)  # Ограничение FPS до 10 кадров в секунду

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Обработка нажатий клавиш для изменения направления
                if event.key == pygame.K_UP:
                    snake.turn('UP')
                elif event.key == pygame.K_DOWN:
                    snake.turn('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.turn('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.turn('RIGHT')

        # Обновление состояния змейки
        try:
            snake.move()
        except Exception as e:
            # Игра заканчивается при столкновении
            print(str(e))
            running = False

        # Проверка, съела ли змейка еду
        if snake.get_head_position() == food.position:
            snake.grow_snake()
            score += 1
            # Генерация новой еды
            food = Food(snake.positions)

        # Отрисовка
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)

        # Отображение счета
        score_text = font.render(f"Счет: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    # Завершение игры
    pygame.quit()
    print(f"Игра окончена! Ваш счет: {score}")

if __name__ == "__main__":
    main()
