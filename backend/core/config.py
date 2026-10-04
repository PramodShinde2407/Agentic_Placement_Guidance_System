import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

APP_NAME = os.getenv(
    "APP_NAME",
    "Agentic Placement Guidance System"
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
).lower() == "true"