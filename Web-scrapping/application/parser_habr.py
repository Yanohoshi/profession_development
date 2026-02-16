import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def fetch_and_parse_habr(URL, KEYWORDS):
    # Создаем движок
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='tm-articles-list__item')

        if not articles:
            articles = soup.find_all('div', class_='tm-article-snippet')

        print(f"Найдено статей на странице: {len(articles)}")
        print("=" * 80)
# ---------------------------------------------------------------------------------------------------------------------
        found_articles = []

        for article in articles:
            article_text = article.get_text().lower()
            if any(keyword.lower() in article_text for keyword in KEYWORDS):

                # Даты
                date_element = article.find('time')
                if date_element and date_element.has_attr('datetime'):
                    date_str = date_element['datetime']
                    try:
                        if 'T' in date_str:
                            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                            date_formatted = date_obj.strftime('%d.%m.%Y')
                        else:
                            date_formatted = date_str
                    except:
                        date_formatted = date_str
                else:
                    date_formatted = "Дата не указана"

                # Заголовки
                title_element = article.find('a', class_='tm-title__link')
                if not title_element:
                    title_element = article.find('a', class_='tm-article-snippet__title-link')

                if title_element:
                    title = title_element.get_text().strip()

                    #Ссылки
                    link_suffix = title_element.get('href', '')
                    if link_suffix:
                        full_link = f"https://habr.com{link_suffix}"
                    else:
                        full_link = "Ссылка не найдена"
                else:
                    title = "Заголовок не найден"
                    full_link = "Ссылка не найдена"

                found_articles.append((date_formatted, title, full_link))

        # Выводим найденные статьи
        if found_articles:
            print(f"\nНайдено статей по ключевым словам {KEYWORDS}: {len(found_articles)}\n")
            for date, title, link in found_articles:
                print(f"{date} – {title} – {link}")
        else:
            print(f"\nСтатей по ключевым словам {KEYWORDS} не найдено.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")