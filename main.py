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
from backend.routes.guidance import router as guidance_router
from backend.routes.role_skill import router as role_skill_router
from backend.routes.company_visit import router as company_visit_router
from backend.routes.eligibility_rule import router as eligibility_rule_router
from backend.routes.eligibility_check import router as eligibility_check_router
from backend.routes.application import router as application_router
from backend.routes.interview_round import router as interview_round_router
from backend.routes.oa_question import router as oa_question_router
from backend.routes.interview_experience import router as interview_experience_router
from backend.routes.project import router as project_router
from backend.routes.resume import router as resume_router
from backend.routes.chat_history import router as chat_history_router
from backend.routes.analytics import router as analytics_router
from backend.routes.analytics import router as analytics_router
from backend.routes.recommendation import router as recommendation_router

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
app.include_router(guidance_router)
app.include_router(role_skill_router)
app.include_router(company_visit_router)
app.include_router(eligibility_rule_router)
app.include_router(eligibility_check_router)
app.include_router(application_router)
app.include_router(interview_round_router)
app.include_router(oa_question_router)
app.include_router(interview_experience_router)
app.include_router(project_router)
app.include_router(resume_router)
app.include_router(chat_history_router)
app.include_router(analytics_router)
app.include_router(analytics_router)
app.include_router(recommendation_router)