# database.py (Example structure)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String, nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Relationship to track clicks
    clicks = db.relationship('Click', backref='url_map', lazy=True)

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url_id = db.Column(db.Integer, db.ForeignKey('short_url.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50))
    user_agent = db.Column(db.String(255))
    # Optional: Add columns for country/city if you use a geolocation API