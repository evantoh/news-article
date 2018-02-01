from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from config import config_options

#initialiing application
app = Flask(__name__,instance_relative_config = True)

#setting pu configuration
app.config.from_object(DevConfig)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
def create_app(config_name):
    app = Flask(__name__)
    #creating the app configurations
    app.config.from_object(config_options[config_name])
     
     #initializing flask extensions
    bootstrap.init_app(app)
    #registering blueprint

    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
     #will add the views and forms
    return app

from app import views