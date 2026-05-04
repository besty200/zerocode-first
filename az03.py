import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import csv
import time
import re

# ======================== 1. ГИСТОГРАММА НОРМАЛЬНОГО РАСПРЕДЕЛЕНИЯ ========================
def task_histogram():
    print("=== 1. Гистограмма нормального распределения ===")

    # Параметры нормального распределения
    mean = 0
    std_dev = 1
    num_samples = 1000

    # Генерация случайных чисел, распределённых по нормальному распределению
    data = np.random.normal(mean, std_dev, num_samples)
    print("Массив данных успешно сгенерирован.\n")

    # Построение гистограммы
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')

    # Настройка графика
    plt.title('Гистограмма нормального распределения', fontsize=15)
    plt.xlabel('Значение', fontsize=12)
    plt.ylabel('Частота', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Добавление линий среднего и стандартного отклонения
    plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Среднее (μ = {mean})')
    plt.axvline(mean + std_dev, color='green', linestyle='dashed', linewidth=2, label=f'μ + σ = {mean + std_dev}')
    plt.axvline(mean - std_dev, color='green', linestyle='dashed', linewidth=2, label=f'μ - σ = {mean - std_dev}')
    plt.legend()

    plt.tight_layout()
    plt.savefig('normal_histogram.png')
    plt.show()
    print("Гистограмма сохранена как 'normal_histogram.png'.\n")

# ======================== 2. ДИАГРАММА РАССЕЯНИЯ ========================
def task_scatter():
    print("=== 2. Диаграмма рассеяния двух наборов случайных данных ===")

    # Генерация двух массивов случайных чисел от 0 до 1
    x = np.random.rand(50)  # массив из 50 случайных чисел
    y = np.random.rand(50)

    print("Массивы случайных данных сгенерированы.")
    print(f"Первый массив (первые 5 элементов): {x[:5]}")
    print(f"Второй массив (первые 5 элементов): {y[:5]}\n")

    # Построение диаграммы рассеяния
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.6, color='purple', edgecolors='white', linewidth=0.5)

    plt.title('Диаграмма рассеяния для двух наборов случайных данных', fontsize=15)
    plt.xlabel('Набор X', fontsize=12)
    plt.ylabel('Набор Y', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('scatter_plot.png')
    plt.show()
    print("Диаграмма рассеяния сохранена как 'scatter_plot.png'.\n")
# ======================== 3. ПАРСИНГ ЦЕН НА ДИВАНЫ (ТОЛЬКО ПЕРВАЯ СТРАНИЦА) ========================
def task_parsing():
    print("=== 3. Парсинг цен на диваны с сайта nonton.ru (только первая страница) ===")

    base_url = "https://samara.nonton.ru"
    catalog_url = base_url + "/mebel/myagkaya-mebel/divany"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    all_prices = []

    try:
        print(f"Загрузка первой страницы каталога: {catalog_url}")
        response = requests.get(catalog_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Поиск блоков с товарами на первой странице
        items = soup.find_all('div', class_='p__offers')
        print(f"Найдено товаров на странице: {len(items)}")

        for item in items:
            try:
                price_element = item.find('meta', {'itemprop': 'price'})
                price_text = price_element.get('content')
                price = int(price_text)


                if price:
                    all_prices.append(price)

            except Exception as e:
                print(f"Ошибка при извлечении цены: {e}")
                continue

        if not all_prices:
            print("Цены не найдены. Возможно, сайт изменил структуру. Проверьте классы элементов.")
            return

        # Сохранение данных в CSV
        csv_file = 'sofa_prices.csv'
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Цена'])
            for price in all_prices:
                writer.writerow([price])
        print(f"\nДанные сохранены в файл '{csv_file}'")

        # Обработка данных - расчёт средней цены
        mean_price = np.mean(all_prices)
        print(f"\nСредняя цена на диваны (по первой странице): {mean_price:,.0f} руб.")

        # Создание гистограммы цен
        plt.figure(figsize=(12, 6))
        plt.hist(all_prices, bins=20, alpha=0.7, color='orange', edgecolor='black')
        plt.axvline(mean_price, color='red', linestyle='dashed', linewidth=2, label=f'Средняя цена: {mean_price:,.0f} руб.')
        plt.title('Гистограмма цен на диваны (первая страница)', fontsize=15)
        plt.xlabel('Цена (руб.)', fontsize=12)
        plt.ylabel('Количество товаров', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.ticklabel_format(style='plain', axis='x')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('sofa_prices_histogram.png')
        plt.show()
        print("Гистограмма цен сохранена как 'sofa_prices_histogram.png'")

    except Exception as e:
        print(f"Ошибка при парсинге: {e}")

if __name__ == "__main__":
    task_histogram()
    task_scatter()
    task_parsing()