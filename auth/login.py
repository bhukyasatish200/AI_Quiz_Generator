"""
Authentication Login Module
"""

from database.db import SessionLocal

from database.crud import (
    get_student_by_registration,
    get_admin_by_username
)

from auth.security import PasswordManager


class LoginManager:

    @staticmethod
    def student_login(
        registration_no: str,
        password: str
    ):

        db = SessionLocal()

        try:

            student = get_student_by_registration(
                db,
                registration_no
            )

            if student is None:
                return False, "Student not found.", None

            if not student.is_active:
                return False, "Account is inactive.", None

            if not PasswordManager.verify_password(
                password,
                student.password
            ):
                return False, "Invalid password.", None

            return True, "Login Successful.", student

        finally:
            db.close()

    @staticmethod
    def admin_login(
        username: str,
        password: str
    ):

        db = SessionLocal()

        try:

            admin = get_admin_by_username(
                db,
                username
            )

            if admin is None:
                return False, "Admin not found.", None

            if not admin.is_active:
                return False, "Account is inactive.", None

            if not PasswordManager.verify_password(
                password,
                admin.password
            ):
                return False, "Invalid password.", None

            return True, "Login Successful.", admin

        finally:
            db.close()