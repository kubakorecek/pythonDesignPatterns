"""
Naive but functional version of website in the flask, more advanced technique could be showed if demand would exist.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)


app.config.update(dict(
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    ,MAIL_SERVER = 'smtp.gmail.com'
    ,MAIL_PORT = 465
    ,MAIL_USE_TLS = False
    ,MAIL_USE_SSL = True
    ,MAIL_USERNAME = 'jakubapp182'
    ,MAIL_PASSWORD = '123hellaS'
    ,ADMINS = ['jakubapp182@gmail.com']
))





mail = Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://kubak182:hellas123@localhost/PythonTutorial"

db = SQLAlchemy(app)
db.create_all()