"""
Authentication Security Module

Handles password hashing and verification.
"""

import bcrypt


class PasswordManager:
    """
    Utility class for password hashing and verification.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a plain-text password.

        Args:
            password (str): User password.

        Returns:
            str: Hashed password.
        """

        password_bytes = password.encode("utf-8")

        hashed = bcrypt.hashpw(
            password_bytes,
            bcrypt.gensalt(rounds=12)
        )

        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(
        password: str,
        hashed_password: str
    ) -> bool:
        """
        Verify password against stored hash.
        """

        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )