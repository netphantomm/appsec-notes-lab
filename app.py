from flask import Flask
app = Flask(__name__)
current_user_id = 1
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
    elif note.get("owner_id") != current_user_id:
        return "Forbidden: You do not have permission to access this note.", 403
        
    else:
        return note.get("text")

