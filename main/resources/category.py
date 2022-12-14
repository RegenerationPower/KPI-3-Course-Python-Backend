from flask_smorest import Blueprint, abort
from flask.views import MethodView
from main.db import CATEGORIES
from flask import request, jsonify

blp = Blueprint("category", __name__, description="category operations")

categoryId = 1


@blp.route("/category/<int:category_id>")
class Category(MethodView):
    def get(self, categories_id):
        try:
            return CATEGORIES[categories_id]
        except KeyError:
            abort(404, message="Category not found")

    def delete(self, categories_id):
        try:
            deleted_category = CATEGORIES[categories_id]
            del CATEGORIES[categories_id]
            return deleted_category
        except KeyError:
            abort(404, message="Category not found")


@blp.route("/category")
class CategoryList(MethodView):
    def get(self):
        return CATEGORIES

    def post(self):
        request_data = {}
        global categoryId
        try:
            categoryId += 1
            request_data["id"] = categoryId
            request_data["title"] = request.get_json()["title"]
        except:
            abort(404, message="Bad request")
        CATEGORIES[categoryId] = request_data
        return jsonify(request_data)
