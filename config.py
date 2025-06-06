import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'una-llave-secreta-muy-segura')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///hotels.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
