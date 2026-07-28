from auth.login import LoginManager

status, message, student = LoginManager.student_login(
    registration_no="2026001",
    password="Admin@123"
)

print("=" * 50)

print("Status :", status)

print("Message :", message)

if student:

    print("Student Name :", student.name)

    print("Department :", student.department)

    print("Year :", student.year)