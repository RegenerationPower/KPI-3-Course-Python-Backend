import datetime
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from main.db import NOTATIONS
from flask import request
from main.schemas import NotationSchema, NotationQuerySchema

blp = Blueprint("note", __name__, description="notation operations")
notationId = 1


@blp.route("/notation/<int:note_id>")
class Note(MethodView):
    @blp.response(200, NotationSchema)
    def get(self, notations_id):
        try:
            return NOTATIONS[notations_id]
        except KeyError:
            abort(404, "Notation not found")

    @blp.response(200, NotationSchema)
    def delete(self, notations_id):
        try:
            deleted_note = NOTATIONS[notations_id]
            del NOTATIONS[notations_id]
            return deleted_note
        except KeyError:
            abort(404, "Notation not found")


@blp.route("/notation")
class NoteList(MethodView):
    @blp.arguments(NotationQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, NotationSchema(many=True))
    def get(self, **kwargs):
        user_notations = [*NOTATIONS.values()]
        try:
            id_user = int(kwargs.get("user_id"))
            try:
                id_category = int(kwargs.get("category_id"))
                print(id_category)
                print(user_notations)
                return list(filter(lambda x: (x.get("user_id") == id_user and x.get("category_id") == id_category), user_notations))
            except TypeError:
                return list(filter(lambda x: (x.get("user_id") == id_user), user_notations))
        except KeyError:
            abort(404, message="Missing user_id")

    @blp.arguments(NotationSchema)
    @blp.response(200, NotationSchema)
    def post(self, request_data):
        notation = {}
        global notationId
        notationId += 1
        notation["id"] = notationId
        notation["user_id"] = request_data["user_id"]
        notation["category_id"] = request_data["category_id"]
        notation["date_of_creating"] = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        notation["price"] = request.get_json()["price"]
        NOTATIONS[notationId] = notation
        return notation
