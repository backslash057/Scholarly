from flask import Flask

from config import db, jwt, init_app


app = Flask(__name__)
init_app(app)


# Register the app routes
from routes.auth_route import auth_bp
from routes.home_route import home_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(home_bp)

# Import database models for create_all()
from models.user import User

@jwt.user_identity_loader
def user_identity_lookup(user):
    return str(user.id)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = int(jwt_data["sub"])
    return User.query.get(identity)


with app.app_context():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    from scripts.create_test_users import create_test_user
    # Create test users automatically
    with app.app_context():
        for i in range(1, 11):
            if not User.query.filter_by(email=f"testuser{i}@example.com").first():
                user = create_test_user(i)
                db.session.add(user)
        db.session.commit()
        print("Test users created.")
    app.run(debug=True)

