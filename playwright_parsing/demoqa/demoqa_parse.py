from playwright.sync_api import sync_playwright
import csv


def get_books_and_publishers(output_path="books.csv"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Ждём, пока таблица полностью отрисуется
        page.goto("https://demoqa.com/books", wait_until="networkidle")
        page.wait_for_selector(".rt-tr-group")

        # Собираем сразу ВСЕ заголовки и ВСЕ издательства
        titles = page.locator(".rt-td:nth-child(2) a").all_inner_texts()
        publishers = page.locator(".rt-td:nth-child(4)").all_inner_texts()

        # Пишем в CSV
        with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Publisher"])
            for title, publisher in zip(titles, publishers):
                title = title.strip()
                publisher = publisher.strip()
                writer.writerow([title, publisher])
                print(f"Title: {title}, Publisher: {publisher}")
        browser.close()

if __name__ == "__main__":
    get_books_and_publishers()
