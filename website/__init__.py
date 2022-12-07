from flask import Flask
from os import path
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
# DB_NAME = "database.db"


def create_app():
    # initilize
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    
    #UIUC = RateMyProfScraper(1112)
    #data = UIUC.professorlist
    
    #df = pd.DataFrame.from_dict(data, columns=['tDept', 'tSid', 'institution_name', 'tFname', 'tMiddlename', 'tLname', 'tid', 'tNumRatings','rating_class','contentType','categoryType','overall_rating'])
    #print(df)

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    # from .models import Professor #ensures db runs on setup
    # #create_database(app)
    # with app.app_context():
    #     db.create_all()

    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
