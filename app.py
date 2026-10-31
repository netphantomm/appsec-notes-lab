from flask import Flask
app = Flask(__name__)
note = {
    "id": 1,
    "owner_id": 1,
    "text": "This is a sample note.",
}

@app.get("/")
def home():
    return "Appsec Notes Lab"

@app.get("/home")
def index():
    return "Welcome to the homepage!"

@app.get("/notes/1")
def show_note():
    return note.get("text")
