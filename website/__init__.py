from flask import Flask
from os import path


def create_app():
    # initilize
    app = Flask(__name__)

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    return app


#source venv/bin/activate  - for activating venv
#running flask app:  flask --app main run