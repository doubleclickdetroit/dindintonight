from __future__ import absolute_import
from django.conf import settings
from core.celery import app
import sendgrid


@app.task
def send_email_to(to, subject, html, text, from_email):
    """
    Method to send a email to a email addresses

    :param to: Email address that you want to add
    :param subject: Subject of the email that you want to send
    :param html: HTML version of the email
    :param text: Text version of the email
    :param from_email: Email address that you want it to show as it coming from
    """
    sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)
    message = sendgrid.Mail(to='rgarrison3@gmail.com', subject='Subject Test', html='Body Test', text='Body Test',
                            from_email='Rob Garrison <rgarrison3@gmail.com>')
    status, msg = sg.send(message)

@app.task
def send_emails_to(to, subject, html, text, from_email):
    """
    Method to send a email to to a array of email addresses

    :param to: Email address array that you want to add
    :param subject: Subject of the email that you want to send
    :param html: HTML version of the email
    :param text: Text version of the email
    :param from_email: Email address that you want it to show as it coming from
    """
    sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)

    message = sendgrid.Mail()
    message.set_subject('Subject Test')
    message.set_html('Body Test')
    message.set_text('Body Test')
    message.set_from('Rob Garrison <rgarrison3@gmail.com>')
    message.add_to(['Example Dude <example@email.com>', 'john@email.com'])
    status, msg = sg.send(message)

@app.task
def send_emails_bcc(to, subject, html, text, from_email):
    """
    Method to send a email BCC to a array of email addresses

    :param to: Email address array that you want to add as BCC
    :param subject: Subject of the email that you want to send
    :param html: HTML version of the email
    :param text: Text version of the email
    :param from_email: Email address that you want it to show as it coming from
    """
    sg = sendgrid.SendGridClient(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD)

    message = sendgrid.Mail()
    message.set_subject('Subject Test')
    message.set_html('Body Test')
    message.set_text('Body Test')
    message.set_from('Rob Garrison <rgarrison3@gmail.com>')
    message.add_bcc(['Example Dude <example@email.com>', 'john@email.com'])
    status, msg = sg.send(message)