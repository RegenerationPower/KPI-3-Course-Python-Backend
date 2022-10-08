from main import app
from flask import jsonify, request
import datetime


users_id = 1
categories_id = 1
notations_id = 1

CATEGORIES = [{
    "id": categories_id,
    "category name": "Shopping",
}]


USERS = [{
    "id": users_id,
    "name": "John",
}]


NOTATION = [{
    "id": notations_id,
    "user_id": users_id,
    "category_id": categories_id,
    "price": 1000,
    "date_of_creating": datetime.date.today()
}]


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['Post'])
def create_category():
    request_data = {}
    global categories_id
    categories_id += 1
    request_data["id"] = categories_id
    try:
        request_data["category name"] = request.get_json()["category name"]
    except:
        request_data["category name"] = "Category name" + str(categories_id)

    CATEGORIES.append(request_data)
    return request_data


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/user", methods=['Post'])
def create_user():
    request_data = {}
    global users_id
    users_id += 1
    request_data["id"] = users_id
    try:
        request_data["name"] = request.get_json()["name"]
    except:
        request_data["name"] = "User" + str(users_id)

    USERS.append(request_data)
    return request_data


@app.route("/notations")
def get_notations():
    return jsonify({"notations": NOTATION})


@app.route("/notation", methods=['Post'])
def create_notation():
    request_data = request.get_json()
    NOTATION.append(request_data)
    return jsonify(request_data)
