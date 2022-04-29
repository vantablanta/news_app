# initialize the application 
from flask import Flask
from .config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

# initialize extensions 
from flask_bootstrap import Bootstrap
bootstrap  = Bootstrap(app)

from app import views