# Import Flask and functions(allows app to show html)
from flask import render_template, url_for, redirect
from main import app
from main.models import Word
from sqlalchemy import func
import string


# When accessed, shows the top page
@app.route('/')
def top():
    return render_template(
        'top.html', type='top')

# When accessed, transfers to game
@app.route('/ufo-coming')
def game():
    alphabets = list(string.ascii_uppercase)
    word = Word.query.order_by(func.random()).first()
    if word:
        secret_word = word.spelling.upper()
        hint = word.category.name
        return render_template(
            'game.html', type='game', alph=alphabets, sec_word=secret_word, hint=hint)
    else:
        return redirect(url_for('top'))

# When accessed, transfers to the administration page
@app.route('/admin')
def admin():
    return render_template('admin.html', type='admin')