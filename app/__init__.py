# initialize the application 
import os
from flask import Flask
from .config import DevConfig



# configurations
app = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'),instance_relative_config = True)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
from app import error