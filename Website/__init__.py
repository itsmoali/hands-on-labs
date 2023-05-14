from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from flask_mqtt import Mqtt


# This is the database
db = SQLAlchemy()
# This is the name of the database
DB_NAME = "database.db"

# This function creates the database
def create_database(db):
    db.drop_all()
    db.create_all()
    print("Database created successfully!")

# This function creates the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'good_grades_are_demanded'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_NAME}'


    db.init_app(app)
    app.app_context().push()

    # This imports the views and auth files
    from Website.views import views
    from Website.auth import auth
    from Website.features import features
    
    # This registers the views and auth files
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(features, url_prefix = '/features')
    

    

    create_database(db)

    # This is the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    from Website.models import User
    # This loads the user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app