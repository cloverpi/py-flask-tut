from flask import render_template, flash, redirect
from app import flask_app
from app.forms import LoginForm

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

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('index')
    return render_template('login.html', title='Login', form=form)
