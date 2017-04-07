from . import mail
from flask.ext.mail import Message
from flask import current_app, render_template
from threading import Thread
from gevent import Greenlet
from gevent import monkey
monkey.patch_socket()


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Greenlet.spawn(send_async_email, app, msg)
    thr.start()
    return thr


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
