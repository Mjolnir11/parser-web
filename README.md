
# Мой GitHub Project

Это мой проект на GitHub. Я опубликовал его прямо из Visual Studio Code.

- 👋 Привет, я @ Mjolnir11
- 🌱 Я сейчас учусь 

<!---
Mjolnir11/Mjolnir11 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->


# install

Весь код написанн при помощи  '<p><a href="https://code.visualstudio.com">Visual Studio Code</a></p>

Чтоб у вас все работало вам нужно установить Python не ниже 3x версии и pip ссылки на них я оставлю ниже 

 <p><a href="https://www.python.org">Ссылка на python</a></p>
 <p><a href="https://pypi.org/project/pip">Ссылка на pip</a></p>
 

Так же вам понадобиться библиотека bs4 она устанавливаеться с помощью pip

```html
pip install bs4 или pip install beautifulsoup4
```
 
 
 # parser-web
 
Данный парсер написан для поиска товаров на сайте https://catalog-sadovod.ru

После запуска парсера вам нужно будет указать ссылку на страницу по который вы хотите спарсить данные если же 
вы выбирите какую то категорию товара то вам нужно будет открыть последнию страницу для парсинга всей категории 
иначе вы спарсите только первые 9 страниц. 

После завершения парсинга у вас появиться файл с названием tovar.csv в нем будут хранится спарсенные данные 

- Название товара 
- Ссылка на товар
- Цена 
- Дата создания

Это сделанно для вашего удобства!!! 

