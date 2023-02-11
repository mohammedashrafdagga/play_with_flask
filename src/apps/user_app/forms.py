from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, EqualTo
# from .validators import custom_username_valid



# Login Form
class LoginForm(FlaskForm):
    username = StringField(label ='username', validators=[
        InputRequired(), Length(min = 10 , max=255)])
    password = PasswordField(label = 'password', validators=[InputRequired()])
    
    
#  Register Form
class RegisterUser(FlaskForm):
    email = EmailField(label='email', validators=[InputRequired()])
    username = StringField(label='username',
                           validators=[InputRequired(), Length(min=10, max=255)])
    password = PasswordField(label = 'password',validators=[InputRequired()])
    confirm_password = PasswordField(label = 'confirm password',validators=[InputRequired(),
                                                                            EqualTo(password)])
    