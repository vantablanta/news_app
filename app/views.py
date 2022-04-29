# routes 
from http.client import responses
from flask import render_template
from app import app
from .request import get_news

@app.route("/")
def index():
    data = get_news()
    return render_template("index.html", responses = data)

@app.route("/news")
def news():
    data = get_news()
    return render_template("news.html", responses = data)