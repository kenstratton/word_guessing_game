import os

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/top')
    def top():
        return render_template('top.html')

    @app.route('/ufo-coming')
    def game():
        alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        return render_template('game.html', alphabets=alphabets)

    return app