from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)  # nullable for Google users
    google_id = db.Column(db.String(255), nullable=True)  # nullable for email users
    auth_method = db.Column(db.String(20), nullable=False)  # "email" or "google"

    mobile_number = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    city_community = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    is_verified = db.Column(db.Boolean, default=False)
    otp_code = db.Column(db.String(6), nullable=True)
    otp_expires_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"