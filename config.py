import os

class Config:
    SECRET_KEY = 'meeting_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meeting.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False