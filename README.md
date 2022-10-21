# Лабораторна 1: Налаштування середовища. Розробка базового REST API
**Виконав:** студент групи ІО-04 - Возниця Дмитро

### Мій [Heroku](http://lab1-python-backend.herokuapp.com/)

Для запуску проєкту локально потрібно мати встановленим Docker aбо Python3

## Python

1. windows: set FLASK_APP=main **або** linux: export FLASK_APP=main
2. flask run

## Docker:

1. docker build --build-arg PORT=5000 . -t main:latest
2. docker-compose build
3. docker-compose up
