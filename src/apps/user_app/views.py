from flask import (render_template, Blueprint, redirect, flash, abort)
from .forms import LoginForm, RegisterUser


user_app = Blueprint('user_app', __name__, url_prefix='/users')


@user_app.route('/')
def user_page():
    return render_template('pages/user/user_page.html')


@user_app.route('/login', methods = ['POST', 'GET'])
def login_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data.lower()
        password = login_form.password.data
        # redirect to another route for user/
        if password in username:
            abort(401)
        else:
            flash(message='Successful Login')
            return redirect(location='/users')
        # return  f"<h2>user name is {username}, and the password is {password}</h2>"
    return render_template('pages/user/login_page.html', login_form=login_form)


@user_app.route('/register', methods = ['POST','GET'])
def register_page():
    register_form = RegisterUser()
    if register_form.validate_on_submit():
        email = register_form.email.data.lower()
        username = register_form.username.data.lower()
        password = register_form.password.data
        confirm_password = register_form.confirm_password.data
        return f"<h2> email: {email}, username: {username}, password: {password},\
            confirm_password: {confirm_password} </h2>"
    return render_template('pages/user/register_page.html', register_form = register_form)