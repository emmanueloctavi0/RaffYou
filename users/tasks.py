
from celery import task
import time
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@task
def send_email_html(subject, template, from_email, recipient_list):
    html_message = render_to_string(template)
    plain_message = strip_tags(html_message)
    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message
    )
    return {
        'message': f'Email send to {recipient_list[0]}',
        'template': template,
    }
