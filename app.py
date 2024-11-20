from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/hello")
def hello():
  return 'Hello'

@app.route("/user/<username>")
def show_username(username):
  return render_template("index.html", username = escape(username))

@app.route("/about")
def about():
  return render_template("about.html")