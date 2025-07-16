from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, set_access_cookies, current_user

from models.user import User
from config import db

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    # check if the user is already authenticated
    if current_user:
        return jsonify({"success": True, "message": "Already looged in"})


    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(email=email).one_or_none()
    if not user or not user.check_password(password):
        return jsonify({"success": False, "message": "Wrong username or password"}), 401

    jwt_token = create_access_token(identity=user)
    return jsonify({"success": True, "message": "Signup succesful", "token": jwt_token})

    # response = make_response(jsonify({"success": True, "message": "Login succesful"}))
    # set_access_cookies(response, jwt_token)
    # return response

@auth_bp.route("/signup", methods=["POST"])
def signup():
    if current_user: return jsonify({"success": True, "message": "Already connected"})

    data = request.get_json()

    name = data.get("name", "").strip()
    if not name: return jsonify({"success": False, "message": "No name specified"})

    surname = data.get("surname", "").strip()
    if not surname: return jsonify({"success": False, "message": "No surname specified"})

    phone_number = data.get("phone_number", "").strip()
    if not phone_number: return jsonify({"success": False, "message": "No phone number specified"})

    email = data.get("email", "").strip()
    if not email: return jsonify({"success": False, "message": "No email address specified"})

    gender = data.get("gender", "").strip()
    if not gender: return jsonify({"success": False, "message": "No gender specified"})

    role = data.get("role", "").strip()
    if role not in ["parent", "teacher", "admin"]: return jsonify({"success": False, "message": "Invalid role specified"})

    password = data.get("password")
    if not password: return jsonify({"success": False, "message": "No password specified"})

    user_exists = User.query.filter_by(email=email).first()
    if user_exists: return jsonify({"success": False, "message": "Email address already in use"})

    user = User(
        name=name,
        surname=surname,
        phone_number=phone_number,
        email=email,
        gender=gender,
        role=role
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    jwt_token = create_access_token(identity=user)

    return jsonify({"success": True, "message": "Signup successful", "token": jwt_token})


@auth_bp.route("/logout", methods=["POST"])
def logout():
    pass
