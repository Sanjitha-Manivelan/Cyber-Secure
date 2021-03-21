import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from cyber.models import User
from CyberSecurity import cyberSecurity

global aes

class LoginForm(FlaskForm):
    global aes

    aes = cyberSecurity("secret")
    print("object")
    #print(aes)
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


class UpdateUserForm(FlaskForm):
    global aes
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    #print(username)
#    print(picture)
    print("Hurray")

    if os.path.isfile("C://Users//maniv//workspace//Cyber-Secure//cyber//static//profile_pics//test.txt"):
        print("ENCRYPT")
        aes.encryptFile("C://Users//maniv//workspace//Cyber-Secure//cyber//static//profile_pics//test.txt")
    else:
        print("DECRYPT")
        aes.decryptFile("C://Users//maniv//workspace//Cyber-Secure//cyber//static//profile_pics//test.txt.enc")

    print("DONE")
    submit = SubmitField('Update')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
