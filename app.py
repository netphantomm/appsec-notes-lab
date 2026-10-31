from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Appsec Notes Lab"

@app.get("/home")
def index():
    return "Welcome to the homepage!"