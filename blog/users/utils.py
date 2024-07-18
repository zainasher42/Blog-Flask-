import os
import secrets
from flask import url_for, current_app
from flask_mail import Message
from blog import mail

def send_reset_email(user):
    token=user.get_reset_token()
    msg=Message('Password Reset Request', sender = 'zainsinger42@gmail.com', recipients=[user.email])

    msg.body = f'''To reset you password, visit the following link:
{url_for('users.reset_token', token = token, _external=True)}
'''
    mail.send(msg)
