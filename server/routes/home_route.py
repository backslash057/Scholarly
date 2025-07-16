from flask import Blueprint, jsonify

from flask_jwt_extended import jwt_required, current_user

home_bp = Blueprint('home_bp', __name__)


@home_bp.route("/", methods=["GET"])
@jwt_required(optional=True)
def home():
    if current_user:
        return jsonify({"authenticated": True, "user": {"name": current_user.username, "email": current_user.email}})
    else:
        return jsonify({"authenticated": False, "message": "Not authenticated yet"})
