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


@app.route("/")
def home():
    return "Lab2 IO-04 Voznytsia Dmytro"


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['POST'])
def create_category():
    request_data = {}
    try:
        request_data["category_name"] = request.get_json()["category_name"]
        global categories_id
        categories_id += 1
        request_data["id"] = categories_id
    except:
        return "Incorrect input"

    CATEGORIES.append(request_data)
    return request_data


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/user", methods=['POST'])
def create_user():
    request_data = {}
    try:
        request_data["name"] = request.get_json()["name"]
        global users_id
        users_id += 1
        request_data["id"] = users_id
    except:
        return "Incorrect input"

    USERS.append(request_data)
    return request_data


@app.route("/notations")
def get_notations():
    return jsonify({"notations": NOTATIONS})


@app.route("/notation", methods=['POST'])
def create_notation():
    request_data = request.get_json()
    try:
        if not (validation("id", request.get_json()["user_id"], USERS) and validation("id",
                request.get_json()["category_id"], CATEGORIES)):
            return "User or category not found"
        global notations_id
        notations_id += 1
        request_data["id"] = notations_id
        request_data["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        request_data["price"] = request.get_json()["price"]
    except:
        return "Error bad request"

    NOTATIONS.append(request_data)
    return request_data


@app.route("/user-notations", methods=["POST"])
def get_user_notations():
    request_data = request.get_json()
    try:
        id_user = request_data["user_id"]
        user_notations = []
        for i in NOTATIONS:
            if i["user_id"] == id_user:
                user_notations.append(i)
        return jsonify(user_notations)
    except:
        return "Error bad request"


@app.route("/user-categories-notations", methods=["POST"])
def get_user_categories_notations():
    request_data = request.get_json()
    try:
        id_user = request_data["user_id"]
        id_category = request_data["category_id"]
        user_notations = []
        for i in NOTATIONS:
            if i["user_id"] == id_user and i["category_id"] == id_category:
                user_notations.append(i)
        return jsonify(user_notations)
    except:
        return "Error bad request"
