from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string


def send_message(name=None, phone=None, email=None, contact_message=None):
    """Send message from a contact form."""

    message = get_template('information/messages/contact_message.txt')
    context = {
            'email': email,
            'phone': phone,
            'name': name,
            'message': contact_message
            }
    body = message.render(context)
    html_message = render_to_string(
        'information/messages/contact_message.html', context)

    title = ('Суботня школа: повідомлення від ' + email)
    msg = EmailMultiAlternatives(
            title,
            body,
            settings.EMAIL_FROM,
            [settings.EMAIL_TO],
            )
    msg.attach_alternative(html_message, "text/html")
    msg.send()
