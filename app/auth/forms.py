from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from flask_wtf import FlaskForm
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Your email address', validators=[Required(),Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    

    email = StringField('your email address', validators=[Required(), Email()])
    username = StringField('your username', validators=[Required()])
    password = PasswordField('password', validators=[Required(), EqualTo('password',message='passwords must match')])
    password_confirm = PasswordField('confirm password', validators=[Required()])
    submit = SubmitField('sign Up')


    def validate_email(self, data_field):
       
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')


    def validate_username(self, data_field):
       
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That user name is already taken. Try another one')




