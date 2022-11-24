import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
#import smtplib # Модуль для работы с почтой

# Получение курса
# Ссылка на нужную страницу
DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
LIRA_RUB = "https://www.google.com/search?q=%D0%BB%D0%B8%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&ei=IMR_Y8qLO8zRqwGTp6L4DQ&ved=0ahUKEwjKm8DzxMf7AhXM6CoKHZOTCN8Q4dUDCA8&uact=5&oq=%D0%BB%D0%B8%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQsQMQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABCABBANOgcIABCABBAKOggIABAHEB4QCjoGCAAQHhANOggIABAeEA8QDToICAAQBRAeEA06BggAEAcQHkoECEEYAEoECEYYAFAAWJ8aYMAhaANwAXgAgAGnAYgBvgmSAQMwLjmYAQCgAQHAAQE&sclient=gws-wiz-serp"

# Заголовки для передачи вместе с URL
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

# Парсим всю страницу
full_page_D = requests.get(DOLLAR_RUB, headers=headers)
full_page_L = requests.get(LIRA_RUB, headers=headers)

# Разбираем через BeautifulSoup
soup_D = BeautifulSoup(full_page_D.content, 'html.parser')
soup_L = BeautifulSoup(full_page_L.content, 'html.parser')

# Получаем нужное для нас значение и возвращаем его
convert_D = soup_D.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
convert_L = soup_L.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

current_converted_price_D = float(convert_D[0].text.replace(",", "."))
current_converted_price_L = float(convert_L[0].text.replace(",", "."))
print(current_converted_price_D)
print(current_converted_price_L)





