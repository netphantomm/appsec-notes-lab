from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask import Flask, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
notes = {
    1: {
        "owner_id": 1,
        "text": "Elliot: repeat Git",
    },
    2: {
        "owner_id": 2,
        "text": "Alex: prepare for the exam",
    },
    3: {
        "owner_id": 3,
        "text": "Joker: Hahahha, I don't wanna kill you! What would I do without you? YOU.. COMPLETE.. MEE",
    },
    4: {
        "owner_id": 1,
        "text": "Elliot: second note",
    }
}

users = {
    "elliot": {
        "id": 1,
        "password_hash": generate_password_hash("training-password"),
    },
    "alex": {
        "id": 2,
        "password_hash": generate_password_hash("alex-password"),
    }
}



@app.get("/")
def home():
    return "Appsec Notes Lab"

@app.get("/home")
def index():
    return "Welcome to the homepage!"

@app.get("/notes/<int:note_id>")
def show_note(note_id):
    current_user_id = session.get("user_id")
    if current_user_id is None:
        return "Authentication required", 401
    note = notes.get(note_id)
    if note is None:
        return "Note not found", 404
    
    if note.get("owner_id") != current_user_id:
        return "Forbidden", 403
    return note.get("text")



@app.post("/login")
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Username and password required", 400
    user = users.get(username)
    if user is None:
        return "Invalid username or password", 401
    
    is_valid = check_password_hash(user["password_hash"], password)
    if not is_valid:
        return "Invalid username or password", 401
    session.clear()
    session["user_id"] = user["id"]
    return "Login in"



@app.post("/logout")
def logout():
    session.clear()
    return "Logged out"