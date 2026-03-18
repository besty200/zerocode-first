import time
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка браузера (headless – работа в фоне)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def get_page(query):
    """Переходит на страницу Википедии по запросу."""
    encoded = urllib.parse.quote(query)
    url = f"https://ru.wikipedia.org/wiki/{encoded}"
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "firstHeading")))
        return True
    except:
        print("Не удалось загрузить страницу. Возможно, статьи нет.")
        return False

def get_title():
    """Возвращает заголовок текущей страницы."""
    try:
        return driver.find_element(By.ID, "firstHeading").text
    except:
        return "Без названия"

def show_paragraphs():
    """Выводит параграфы статьи по одному."""
    try:
        content = driver.find_element(By.ID, "mw-content-text")
        paras = content.find_elements(By.TAG_NAME, "p")
    except:
        print("Не удалось найти параграфы.")
        return

    if not paras:
        print("В этой статье нет параграфов (возможно, страница значений).")
        return

    print(f"\n--- {get_title()} ---")
    for p in paras:
        text = p.text.strip()
        if text:
            print(f"\n{text[:300]}..." if len(text) > 300 else f"\n{text}")
            inp = input("Нажмите Enter для продолжения (или 'q' для выхода) -> ")
            if inp.lower() == 'q':
                break
        time.sleep(0.1)

def show_links():
    """Показывает внутренние ссылки и возвращает URL выбранной."""
    try:
        content = driver.find_element(By.ID, "mw-content-text")
        all_links = content.find_elements(By.TAG_NAME, "a")
    except:
        print("Не удалось найти ссылки.")
        return None

    # Собираем ссылки на статьи (без служебных страниц)
    links = []
    for a in all_links:
        href = a.get_attribute("href")
        if href and href.startswith("https://ru.wikipedia.org/wiki/") and ":" not in href.split("/")[-1]:
            title = a.text.strip()
            if title:
                links.append((title, href))

    # Убираем дубликаты и ограничиваем 20 ссылками
    unique = []
    seen = set()
    for title, url in links:
        if url not in seen and len(unique) < 20:
            unique.append((title, url))
            seen.add(url)

    if not unique:
        print("Нет связанных страниц.")
        return None

    print("Связанные страницы:")
    for i, (title, _) in enumerate(unique, 1):
        print(f"{i}. {title}")

    choice = input("Введите номер для перехода (0 – отмена): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(unique):
        return unique[int(choice)-1][1]
    return None

def main():
    print("=== Консольный поиск в Википедии (Selenium) ===")
    query = input("Введите поисковый запрос: ").strip()
    if not query:
        print("Запрос пуст.")
        driver.quit()
        return

    if not get_page(query):
        driver.quit()
        return

    while True:
        print(f"\nТекущая статья: {get_title()}")
        print("Меню:")
        print("1. Листать параграфы")
        print("2. Перейти на связанную страницу")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ").strip()

        if choice == '1':
            show_paragraphs()
        elif choice == '2':
            url = show_links()
            if url:
                driver.get(url)
                try:
                    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "firstHeading")))
                except:
                    print("Не удалось загрузить новую страницу.")
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

    driver.quit()

if __name__ == "__main__":
    main()