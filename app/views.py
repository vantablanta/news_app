# routes 
from http.client import responses
from flask import render_template
from app import app
from .request import get_news, get_sources

@app.route("/")
def index():
    sources = get_sources()
    news = get_news()
    return render_template("index.html", sources = sources, news = news )

# @app.route("/news")
# def news():
#     sources = get_news()
#     return render_template("news.html", sources = sources)