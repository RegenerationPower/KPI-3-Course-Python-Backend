import datetime
from flask import jsonify, request
from main import app


user_id = 1
categories_id = 1
notation_id = 1

CATEGORIES = [{
    "id": categories_id,
    "name": "Shopping",
}]


USERS = [{
    "id": user_id,
    "name": "John",
}]


NOTATION = [{
    "id": notation_id,
    "user_id": user_id,
    "category_id": categories_id,
    "price": 1000,
    "date_of_creating": datetime.date.today()
}]


@app.route("/categories")
def get_categories():
    return jsonify({"categories": CATEGORIES})


@app.route("/category", methods=['Post'])
def create_category():
    request_data = request.get_json()
    CATEGORIES.append(request_data)
    return jsonify(request_data)


@app.route("/users")
def get_users():
    return jsonify({"users": USERS})


@app.route("/user", methods=['Post'])
def create_user():
    request_data = request.get_json()
    USERS.append(request_data)
    return jsonify(request_data)


@app.route("/notations")
def get_notations():
    return jsonify({"notations": NOTATION})


@app.route("/notation", methods=['Post'])
def create_notation():
    request_data = request.get_json()
    NOTATION.append(request_data)
    return jsonify(request_data)
