from auth.register import StudentRegistration


status, message = StudentRegistration.register(

    registration_no="2026001",

    name="Bhukya Satish",

    email="satish@gmail.com",

    mobile="9876543210",

    department="Computer Science",

    year="3rd Year",

    password="Admin@123"

)

print(status)

print(message)