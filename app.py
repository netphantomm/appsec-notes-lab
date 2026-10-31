from flask import Flask
app = Flask(__name__)
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
}

@app.get("/")
def home():
    return "Appsec Notes Lab"

@app.get("/home")
def index():
    return "Welcome to the homepage!"

@app.get("/notes/<int:note_id>")
def show_note(note_id):
    note = notes.get(note_id)
    
    if note is None:
        return "Note not found", 404
    else:
        return note.get("text")

