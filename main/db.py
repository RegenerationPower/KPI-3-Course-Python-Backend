import datetime

users_id = 1
categories_id = 1
notations_id = 1

CATEGORIES = [{
    "id": categories_id,
    "category_name": "Shopping",
}]


USERS = [{
    "id": users_id,
    "name": "John",
}]


NOTATIONS = [{
    "id": notations_id,
    "user_id": users_id,
    "category_id": categories_id,
    "price": 1000,
    "date_of_creating": datetime.datetime.now()
}]

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()