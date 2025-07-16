from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()


def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://backslash057:root@localhost:5432/scholarly'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    app.config['JWT_SECRET_KEY'] = 'super_secret_key'
    app.config['JWT_TOKEN_LOCATION'] = ["headers", "cookies", "json"]

    # Configuration to force cookies on https only when defining them
    # change for production
    app.config["JWT_COOKIE_SECURE"] = False

    jwt.init_app(app)