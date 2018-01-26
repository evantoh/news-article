from flask import Flask
from .config import DevConfig

#initialiing application
app = Flask(__name__)

#setting pu configuration
app.config.from_object(DevConfig)
from app import views