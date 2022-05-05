import os

DATABASE_URL = os.getenv('DATABASE_URL')

class Config:
  DEBUG = True
  SQLALCHEMY_ECHO = True
  SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/cat_collector'
  SQLALCHEMY_TRACK_MODIFICATIONS = False