from app import db
from app import app

with app.app_context():
    db.create_all()
    print("Baza danych została zainicjowana.")
