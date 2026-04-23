import pandas as pd
import numpy as np

# Шаг 1: Создаём DataFrame с данными
# Генерируем случайные оценки от 2 до 5 для 10 учеников по 5 предметам
np.random.seed(42)  # Для воспроизводимости результатов

data = {
    'Ученик': [f'Ученик_{i}' for i in range(1, 11)],
    'Математика': np.random.randint(2, 6, size=10),
    'Физика': np.random.randint(2, 6, size=10),
    'Химия': np.random.randint(2, 6, size=10),
    'Биология': np.random.randint(2, 6, size=10),
    'История': np.random.randint(2, 6, size=10)
}

df = pd.DataFrame(data)

# Шаг 2: Выводим первые несколько строк DataFrame
print("Выводим первые 5 записей нашего DataFrame:")
print(df.head())
print("\n" + "="*50 + "\n")

# Шаг 3: Вычисляем среднюю оценку по каждому предмету
print("Средняя оценка по каждому предмету:")
mean_scores = df.drop('Ученик', axis=1).mean()
print(mean_scores)
print("\n" + "="*50 + "\n")

# Шаг 4: Вычисляем медианную оценку по каждому предмету
print("Медианная оценка по каждому предмету:")
median_scores = df.drop('Ученик', axis=1).median()
print(median_scores)
print("\n" + "="*50 + "\n")

print(f"Стандартное отклонение по Математике - {df['Математика'].std()}")
print("\n" + "="*50 + "\n")

# Шаг 5: Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IRQ = Q3_math - Q1_math

print("Квартили для оценок по математике:")
print(f"Q1 (25-й перцентиль): {Q1_math}")
print(f"Q3 (75-й перцентиль): {Q3_math}")
print(f"IRQ (межквартальный размах): {IRQ}")
