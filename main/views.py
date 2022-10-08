from main import app
from flask import jsonify, request
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


def validation(key, value, arr):
    for i in arr:
        if i[key] == value:
            return True
    return False


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
        request_data["category_name"] = request.get_json()["category_name"]
    except:
        return "Incorrect input"

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
        return "Incorrect input"

    USERS.append(request_data)
    return request_data


@app.route("/notations")
def get_notations():
    return jsonify({"notations": NOTATIONS})


@app.route("/notation", methods=['Post'])
def create_notation():
    request_data = request.get_json()
    global note_id
    note_id += 1
    try:
        if not (validation("id", request.get_json()["user_id"], USERS) and validation("id",
                request.get_json()["category_id"], CATEGORIES)):
            return "User or category not found"
        request_data["id"] = note_id
        request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        request_data["price"] = request.get_json()["price"]
    except:
        return "Error bad request"

    NOTATIONS.append(request_data)
    return request_data
