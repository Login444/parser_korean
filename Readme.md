# Простой скрипт для парсинга сайта по обучению корейскому языку.

## Задача:
На сайте по обучению корейскому языку необходимо найти все уроки по определенной теме, вытащить все материалы со страницы с уроком и сохранить в отдельный файл (например Word).
Назавание каждого файла - это название темы урока.

## Реализация:
Т.к. на сайте есть "защита от роботов", было принято решение имитировать работу браузера с помощью библиотеки *Selenium*.
Скрипт получает данные логина и пароля из файла .env при помощи библиотеки *python-dotenv*, далее выполняется авторизация на странице курсов, далее выполняется поиск интересующего курса.
После чего скрипт поочередно заходит на страницу каждого урока, копирует все материалы и сохраняет их в отдельный файл Word.
Название файла берется из названия урока указанного на веб-странице.
