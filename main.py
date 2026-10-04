from fastapi import FastAPI

from sqlalchemy import text

from backend.database.connection import engine

from backend.routes.student import router as student_router
from backend.routes.role import router as role_router
from backend.routes.skill import router as skill_router
from backend.routes.student_skill import router as student_skill_router
from backend.routes.company import router as company_router
from backend.routes.placement import router as placement_router
from backend.routes.auth import router as auth_router
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

app.include_router(student_router)
app.include_router(role_router)
app.include_router(skill_router)
app.include_router(student_skill_router)
app.include_router(company_router)
app.include_router(placement_router)
app.include_router(auth_router)