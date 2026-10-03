from fastapi import FastAPI

from sqlalchemy import text

from backend.database.connection import engine


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Agentic Placement Guidance System API is running"
    }


@app.get("/test-db")
def test_db():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT current_database(), current_user")
        )

        row = result.fetchone()

    return {
        "database": row[0],
        "user": row[1]
    }