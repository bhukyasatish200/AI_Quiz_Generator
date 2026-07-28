"""
Student Registration
"""

import re

from database.db import SessionLocal
from database.models import Student

from database.crud import (
    registration_exists,
    email_exists,
    create_student
)

from auth.security import PasswordManager


class StudentRegistration:

    @staticmethod
    def validate_email(email: str):

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.match(pattern, email) is not None

    @staticmethod
    def validate_password(password: str):

        if len(password) < 8:
            return False

        return True

    @staticmethod
    def register(
        registration_no,
        name,
        email,
        mobile,
        department,
        year,
        password
    ):

        db = SessionLocal()

        try:

            if registration_exists(db, registration_no):
                return False, "Registration Number already exists."

            if email_exists(db, email):
                return False, "Email already registered."

            if not StudentRegistration.validate_email(email):
                return False, "Invalid email."

            if not StudentRegistration.validate_password(password):
                return (
                    False,
                    "Password should contain at least 8 characters."
                )

            hashed_password = PasswordManager.hash_password(password)

            student = Student(
                registration_no=registration_no,
                name=name,
                email=email,
                mobile=mobile,
                department=department,
                year=year,
                password=hashed_password
            )

            create_student(db, student)

            return True, "Student Registered Successfully."

        except Exception as e:

            db.rollback()

            return False, str(e)

        finally:

            db.close()