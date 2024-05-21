import os

class Config:
    SECRET_KEY = os.environ.get('SECRECT_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://Recordaty:recordaty_ALX!@localhost/recordaty'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
