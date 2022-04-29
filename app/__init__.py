# initialize the application 
from flask import Flask
from .config import DevConfig

# configurations
app = Flask(__name__, instance_relative_config = True)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initialize extensions 
from flask_bootstrap import Bootstrap
bootstrap  = Bootstrap(app)

from app import views