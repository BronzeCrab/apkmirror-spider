Что сделал:
=====

Сделал базовый спайдер на `Scrapy`, который парсит основную информацию по apk пакетам, пытался
использовать список прокси для того, чтобы обойти защиту. К сожалению добиться стабильной работы не удалось.

В файле `apkmirror/list.txt` лежат прокси с сайта `https://free-proxy-list.net/`

Поведение прокси описано в файле `apkmirror/apkmirror/settings.py`

Как запустить (работает плохо):
=====

`pip install -r requirements.txt`

Как заустить паука из корневой папки проекта:

`scrapy crawl apkmirror_spider -o output.csv -t csv`