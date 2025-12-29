import bcrypt
import sqlite3
from email_validator import validate_email, EmailNotValidError
import requests 

conn = sqlite3.connect("data/users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password BLOB,
    email TEXT
)
""")
conn.commit()


def create_hash(password):
    password_bytes = password.encode("utf-8")
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())


def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode("utf-8"), stored_password)


def register_account(username, password, email):
    try:
        cursor.execute(
            "SELECT id FROM users WHERE username = ?",
            (username,)
        )
        if cursor.fetchone():
            return {
                "status": "error",
                "message": "Username already exists"
            }


        hashed_pw = create_hash(password)

        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, hashed_pw, email)
        )
        conn.commit()

        return {
            "status": "success",
            "message": "Registration successful"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

def check_email(email):
    try:
        v = validate_email(email)
        normalized_email = v.email
        return True, normalized_email
    except EmailNotValidError as e:
        return False, str(e)


def login_account(username, password):
    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()

    if user is None:
        return {
            "status": "error",
            "message": "User not found"
        }

    stored_password = user[0]

    if verify_password(stored_password, password):
        return {
            "status": "success",
            "message": "Login successful"
        }
    else:
        return {
            "status": "error",
            "message": "Wrong password"
        }


def send_mail(username):
    pass

