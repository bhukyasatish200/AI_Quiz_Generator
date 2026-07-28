from auth.login import LoginManager

status, message, admin = LoginManager.admin_login(
    username="admin",
    password="Admin@123"
)

print("=" * 50)

print(status)

print(message)

if admin:

    print(admin.full_name)

    print(admin.email)