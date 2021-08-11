import requests
from bs4 import BeautifulSoup
import csv
import os


url = ''
headers = {
    'accept': '*/*'
              'user-agent' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 OPR/76.0.4017.123'
}
file = 'tovar.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', attrs={'class': 'cm-history ty-pagination__item cm-ajax'})
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ty-column5')

    tovar = []
    for item in items:
        tovar.append({
            'title': item.find('a', attrs={'class': 'product-title'}).get_text(strip=True),
            'link': item.find('a')['href'],
            'price': item.find('span', attrs={'class': 'ty-price'}).get_text(strip=True),
            'date': item.find('span', attrs={'class': 'bc-creation-date-label'}).get_text(strip=True),

        })
    return tovar


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название товара', 'Ссылка на товар', 'Цена', 'Дата создания '])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['date']])

def parse():
    url = input('Введите ссылку url: ')
    url = url.strip()
    html = get_html(url)
    if html.status_code == 200:
        tovar = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страниц {page} из {pages_count}...')
            html = get_html(url, params={'page': page})
            tovar.extend(get_content(html.text))
        save_file(tovar, file)
        print(f'Полученно {len(tovar)} товаров')
        os.startfile(file)
    else:
        print('Ошибка')


parse()