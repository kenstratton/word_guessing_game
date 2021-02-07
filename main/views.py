# Import Flask and functions(allows app to show html)
from flask import Flask, render_template, url_for
from main import app
from main.models import Word
from sqlalchemy import func
import string


# When accessed '/', shows the top page
@app.route('/')
def top():
    return render_template(
        'top.html', type="top")

# When accessed '/ufo-coming', transfers to game
@app.route('/ufo-coming')
def game():
    alphabets = list(string.ascii_uppercase)
    word = Word.query.order_by(func.random()).first()
    secret_word = word.spelling.upper()
    hint = word.category.name
    return render_template(
        'game.html', type="game", alph=alphabets, sec_word=secret_word, hint=hint)