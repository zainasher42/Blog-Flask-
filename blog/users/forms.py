from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from flask_login import current_user
from blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators = 
                           [DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
                                   validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists.')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators = 
                           [Optional(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[Optional(),Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg','png', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if(username.data!=current_user.username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists.')
        else:
            raise ValidationError('Username same as earlier.')
        
    def validate_email(self,email):
        if(email.data!=current_user.email):
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exists.')
        else:
            raise ValidationError('Email same as earlier.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('No Account With This Email. Please Register.')
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password',
                           validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',
                                   validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Reset Password')