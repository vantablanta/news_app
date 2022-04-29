# routes 
from flask import render_template
from app import app
from .request import get_news

@app.route("/")
def index():
    response = get_news()
    return render_template("index.html",data = response)