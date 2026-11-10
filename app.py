from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Viral Protection"


@app.route("/about")
def about():
    return "Viral Protection is a safe friendly neighborhood software protection service in Coral Gables."