from flask import Flask

# from ..main import register
from .forms import LoginForm, RegistrationForm


def create_app():
  app = Flask(__name__)
  # app.config['SECRET_KEY'] = 'your_secret_key'

  with app.app_context():
    from . import views

    LoginForm()
    RegistrationForm()

  return app
