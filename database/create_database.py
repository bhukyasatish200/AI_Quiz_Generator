"""
Create Database
"""

from database.db import Base, engine

# Import all models
import database.models

def create_database():

    Base.metadata.create_all(bind=engine)

    print("=" * 60)
    print("Database Created Successfully")
    print("=" * 60)


if __name__ == "__main__":
    create_database()