from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask object
app = Flask(__name__)
app.config.from_object('word_guessing_game.config')

db = SQLAlchemy(app)

import word_guessing_game.views