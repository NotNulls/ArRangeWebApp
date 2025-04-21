from threading import Thread
from flask import current_app
from flask_mail import Message
from flask import current_app


def send_async_email(app, msg):
    from app import mail
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, body, to
               ,attachments=None, sync=False):
    from app import mail
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
