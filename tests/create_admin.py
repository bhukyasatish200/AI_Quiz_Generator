from database.db import SessionLocal
from database.models import Admin

from auth.security import PasswordManager

db = SessionLocal()

admin = Admin(
    username="admin",
    password=PasswordManager.hash_password("Admin@123"),
    full_name="System Administrator",
    email="admin@example.com"
)

db.add(admin)

db.commit()

db.close()

print("Admin Created Successfully")