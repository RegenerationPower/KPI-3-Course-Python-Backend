import datetime
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from main.db import NOTATIONS
from flask import request

blp = Blueprint("note", __name__, description="notation operations")
notationId = 1


@blp.route("/notation/<int:note_id>")
class Note(MethodView):
    def get(self, notations_id):
        try:
            return NOTATIONS[notations_id]
        except KeyError:
            abort(404, "Notation not found")

    def delete(self, notations_id):
        try:
            deleted_note = NOTATIONS[notations_id]
            del NOTATIONS[notations_id]
            return deleted_note
        except KeyError:
            abort(404, "Notation not found")


@blp.route("/notation")
class NoteList(MethodView):
    def get(self):
        user_notations= [*NOTATIONS.values()]
        request_data = request.get_json()
        try:
            id_user = request_data["user_id"]
            try:
                id_category = request_data["category_id"]
                return list(filter(lambda x: (x.get("user_id") == id_user and x.get("category_id") == id_category), user_notations))
            except KeyError:
                return list(filter(lambda x: (x.get("user_id") == id_user), user_notations))
        except KeyError:
            abort(404, message="Missing user_id")

    def post(self):
        request_data = request.get_json()
        note = {}
        global notationId
        try:
            if not ("user_id" in request_data or "category_id" in request_data or "price" in request_data):
                abort(400, message="Bad request")
            notationId += 1
            note["id"] = notationId
            note["user_id"] = request_data["user_id"]
            note["category_id"] = request_data["category_id"]
            note["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            note["price"] = request.get_json()["price"]
        except KeyError:
            abort(404, message="Bad request")

        NOTATIONS[notationId] = note
        return note