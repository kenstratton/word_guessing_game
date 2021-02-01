# Import Flask and functions(allows app to show html)
from flask import Flask, render_template, url_for
from main import app

# when accessed '/', shows the top page
@app.route('/')
def top():
    return render_template('top.html')

# When accessed '/ufo-coming', transfers to game
@app.route('/ufo-coming')
def game():
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return render_template('game.html', alphabets=alphabets)