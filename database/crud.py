"""
CRUD Operations for AI Quiz Generator
"""

from sqlalchemy.orm import Session

from database.models import (
    Admin,
    Student,
    Material,
    MaterialText,
    Question,
    Quiz,
    QuizQuestion,
    Attempt,
    StudentAnswer,
    Result
)

# ==========================================================
# ADMIN
# ==========================================================

def create_admin(db: Session, admin):
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin


def get_admin_by_username(db: Session, username):
    return db.query(Admin).filter(
        Admin.username == username
    ).first()


# ==========================================================
# STUDENT
# ==========================================================

def create_student(db: Session, student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_student_by_registration(db: Session, registration_no):
    return db.query(Student).filter(
        Student.registration_no == registration_no
    ).first()


def get_student_by_email(db: Session, email):
    return db.query(Student).filter(
        Student.email == email
    ).first()


# ==========================================================
# MATERIAL
# ==========================================================

def create_material(db: Session, material):
    db.add(material)
    db.commit()
    db.refresh(material)
    return material


def get_material(db: Session, material_id):
    return db.query(Material).filter(
        Material.id == material_id
    ).first()


# ==========================================================
# MATERIAL TEXT
# ==========================================================

def save_extracted_text(db: Session, text):
    db.add(text)
    db.commit()
    db.refresh(text)
    return text


# ==========================================================
# QUESTIONS
# ==========================================================

def create_question(db: Session, question):
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def get_all_questions(db: Session):
    return db.query(Question).all()


# ==========================================================
# QUIZ
# ==========================================================

def create_quiz(db: Session, quiz):
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz


def add_question_to_quiz(db: Session, quiz_question):
    db.add(quiz_question)
    db.commit()
    db.refresh(quiz_question)
    return quiz_question


# ==========================================================
# ATTEMPTS
# ==========================================================

def create_attempt(db: Session, attempt):
    db.add(attempt)
    db.commit()
    db.refresh(attempt)
    return attempt


# ==========================================================
# ANSWERS
# ==========================================================

def save_student_answer(db: Session, answer):
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer


# ==========================================================
# RESULTS
# ==========================================================

def save_result(db: Session, result):
    db.add(result)
    db.commit()
    db.refresh(result)
    return result