from flask import render_template
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'CloverPi'}
    posts = [
        {
            'author': {'username': 'Potato'},
            'body': 'I have many eyes'
        },
        {
            'author': {'username': 'Banana'},
            'body': 'Why don\'t you just split'
        }
    ]
    return render_template('index.html', user=user, posts=posts)
