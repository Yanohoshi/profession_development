from application.parser_habr import fetch_and_parse_habr
# Определяем список ключевых слов
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
# URL для парсинга
URL = 'https://habr.com/ru/articles/' # <-----------------\/
# feed - без разделения (статьи, новости, посты - в перемешку)
# articles - с разделением (имеются активные вкладки статьи, новости, посты)

fetch_and_parse_habr(URL, KEYWORDS)