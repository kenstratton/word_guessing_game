import os

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/top')
    def top():
        return render_template('top.html')

    return app