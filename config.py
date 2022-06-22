import os

from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(base_dir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-duper-difficult-password-666'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(base_dir, 'vtmchars.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
