from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

# Шаг 2: Конкретные реализации оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self) -> str:
        return "наносит удар из лука"

# Можно легко добавить новое оружие без изменения Fighter или Monster
class Axe(Weapon):
    def attack(self) -> str:
        return "наносит удар топором"

# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self) -> str:
        return f"Боец {self.weapon.attack()}."

# Простой класс монстра
class Monster:
    def __init__(self):
        self.alive = True

    def take_damage(self):
        self.alive = False
        return "Монстр побежден!"

# Шаг 4: Механизм боя (закрыт для модификации)
def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    if monster.alive:
        print(monster.take_damage())

# Демонстрация работы программы
if __name__ == "__main__":
    # Создаём монстра
    monster = Monster()

    # Создаём бойца с мечом
    fighter = Fighter(Sword())
    print("Боец выбирает меч.")
    battle(fighter, monster)

    print()  # Пустая строка для разделения боёв

    # Меняем оружие на лук
    fighter.change_weapon(Bow())
    monster = Monster()  # Новый монстр для второго боя
    print("Боец выбирает лук.")
    battle(fighter, monster)

    print()  # Пустая строка для разделения боёв

    # Добавляем новое оружие без изменения Fighter или battle!
    fighter.change_weapon(Axe())
    monster = Monster()
    print("Боец выбирает топор.")
    battle(fighter, monster)