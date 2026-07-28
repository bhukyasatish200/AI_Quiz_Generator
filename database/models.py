from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text
)

from sqlalchemy.orm import relationship

from database.db import Base

class Admin(Base):

    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)

    username = Column(String(50), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    full_name = Column(String(150))

    email = Column(String(150), unique=True)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    registration_no = Column(
        String(30),
        unique=True,
        nullable=False
    )

    name = Column(String(150), nullable=False)

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    mobile = Column(String(20))

    department = Column(String(100))

    year = Column(String(20))

    password = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    attempts = relationship(
        "Attempt",
        back_populates="student",
        cascade="all, delete-orphan"
    )

class Material(Base):

    __tablename__ = "materials"

    id = Column(Integer, primary_key=True)

    title = Column(String(250), nullable=False)

    filename = Column(String(250), nullable=False)

    file_type = Column(String(20))

    uploaded_by = Column(String(100))

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    extracted = Column(
        Boolean,
        default=False
    )

    text = relationship(
        "MaterialText",
        back_populates="material",
        uselist=False,
        cascade="all, delete-orphan"
    )

class MaterialText(Base):

    __tablename__ = "material_text"

    id = Column(Integer, primary_key=True)

    material_id = Column(
        Integer,
        ForeignKey("materials.id"),
        unique=True
    )

    extracted_text = Column(Text)

    total_words = Column(Integer)

    total_characters = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    material = relationship(
        "Material",
        back_populates="text"
    )

class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    question = Column(Text, nullable=False)

    option_a = Column(Text, nullable=False)

    option_b = Column(Text, nullable=False)

    option_c = Column(Text, nullable=False)

    option_d = Column(Text, nullable=False)

    correct_answer = Column(
        String(1),
        nullable=False
    )

    explanation = Column(Text)

    difficulty = Column(String(20))

    topic = Column(String(100))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    quizzes = relationship(
        "QuizQuestion",
        back_populates="question",
        cascade="all, delete-orphan"
    )

class Quiz(Base):

    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)

    title = Column(String(200), nullable=False)

    description = Column(Text)

    total_questions = Column(Integer, default=0)

    total_marks = Column(Float, default=0)

    time_limit = Column(Integer)     # Minutes

    is_published = Column(Boolean, default=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    questions = relationship(
        "QuizQuestion",
        back_populates="quiz",
        cascade="all, delete-orphan"
    )

    attempts = relationship(
        "Attempt",
        back_populates="quiz",
        cascade="all, delete-orphan"
    )

class QuizQuestion(Base):

    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True)

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id")
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    marks = Column(Float, default=1)

    quiz = relationship(
        "Quiz",
        back_populates="questions"
    )

    question = relationship(
        "Question",
        back_populates="quizzes"
    )

class Attempt(Base):

    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id")
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    submitted_at = Column(DateTime)

    score = Column(Float, default=0)

    percentage = Column(Float, default=0)

    status = Column(
        String(20),
        default="Completed"
    )

    student = relationship(
        "Student",
        back_populates="attempts"
    )

    quiz = relationship(
        "Quiz",
        back_populates="attempts"
    )

    answers = relationship(
        "StudentAnswer",
        back_populates="attempt",
        cascade="all, delete-orphan"
    )

    result = relationship(
        "Result",
        back_populates="attempt",
        uselist=False,
        cascade="all, delete-orphan"
    )

class StudentAnswer(Base):

    __tablename__ = "student_answers"

    id = Column(Integer, primary_key=True)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id")
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    selected_answer = Column(String(1))

    is_correct = Column(Boolean)

    marks_obtained = Column(Float, default=0)

    attempt = relationship(
        "Attempt",
        back_populates="answers"
    )

    question = relationship("Question")

class Result(Base):

    __tablename__ = "results"

    id = Column(Integer, primary_key=True)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id"),
        unique=True
    )

    total_questions = Column(Integer)

    correct_answers = Column(Integer)

    wrong_answers = Column(Integer)

    unanswered = Column(Integer)

    total_marks = Column(Float)

    obtained_marks = Column(Float)

    percentage = Column(Float)

    grade = Column(String(5))

    remarks = Column(String(200))

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    attempt = relationship(
        "Attempt",
        back_populates="result"
    )