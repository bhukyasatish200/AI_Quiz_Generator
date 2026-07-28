"""
Test Password Hashing
"""

from auth.security import PasswordManager


password = "Admin@123"

hashed = PasswordManager.hash_password(password)

print("=" * 50)

print("Original Password")

print(password)

print("=" * 50)

print("Hashed Password")

print(hashed)

print("=" * 50)

print("Correct Password")

print(
    PasswordManager.verify_password(
        "Admin@123",
        hashed
    )
)

print("=" * 50)

print("Wrong Password")

print(
    PasswordManager.verify_password(
        "WrongPassword",
        hashed
    )
)