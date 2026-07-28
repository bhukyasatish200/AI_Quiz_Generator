"""
Project Settings
"""

from pathlib import Path

# Root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DATABASE_NAME = "quiz.db"
DATABASE_PATH = BASE_DIR / "database" / DATABASE_NAME
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Upload folders
UPLOAD_FOLDER = BASE_DIR / "uploads"
EXTRACTED_TEXT_FOLDER = BASE_DIR / "extracted_text"
GENERATED_QUESTION_FOLDER = BASE_DIR / "generated_questions"

# AI Models
MODEL_FOLDER = BASE_DIR / "models"

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
LLM_MODEL = "microsoft/Phi-3-mini-4k-instruct"