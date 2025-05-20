from flask import Blueprint, jsonify
from app.database.models import FireAlert
from app.database.db_utils import db

api_bp = Blueprint('api', __name__)

@api_bp.route("/fires", methods=["GET"])
def get_fires():
    alerts = FireAlert.query.all()
    return jsonify([a.to_dict() for a in alerts])
