import random
from app import app
from config import db
from models.user import User

roles = ["parent", "teacher", "admin"]
genders = ["M", "F"]

def random_phone():
    return f"+1{random.randint(1000000000, 9999999999)}"

def create_test_user(idx):
    user = User(
        name=f"Test{idx}",
        surname=f"User{idx}",
        phone_number=random_phone(),
        email=f"testuser{idx}@example.com",
        gender=random.choice(genders),
        role=random.choice(roles)
    )
    user.set_password("password123")
    return user

with app.app_context():
    for i in range(1, 11):
        if not User.query.filter_by(email=f"testuser{i}@example.com").first():
            user = create_test_user(i)
            db.session.add(user)
    db.session.commit()
    print("Test users created.")
