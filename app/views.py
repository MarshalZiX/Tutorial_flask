from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/index', methods =['GET', 'POST'])
def login():
    form =LoginForm()
    return render_template('login.html', title ='Sign In', form =form)
