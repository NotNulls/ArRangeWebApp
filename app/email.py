from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail
from flask import current_app


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, body, to
               ,attachments=None, sync=False):
    msg = Message(sender=sender, recipients=["di.ar.34@gmail.com"])
    msg.body = body
    msg.subject = subject
    msg.reply_to = to
    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email,
               args=(current_app._get_current_object(), msg)).start()
