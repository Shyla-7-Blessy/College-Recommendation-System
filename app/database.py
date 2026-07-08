from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgre@localhost:5432/college_recommendation"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("Database Connected Successfully!")
except Exception as e:
    print("Database Connection Failed")
    print(e)
