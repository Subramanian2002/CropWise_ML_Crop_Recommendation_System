from app import app, db, User, Prediction
from sqlalchemy import text, inspect


with app.app_context():
    # --- Create tables if they don't exist ---
    db.create_all()

    # --- Show all tables ---
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        tables = [row[0] for row in result]
        print("Tables in database:", tables)

#     
