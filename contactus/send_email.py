from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.db.models import Sum
from .settings import EMAIL_FROM
from decouple import config

owner_email = config('OWNER_EMAIL')




class Email:


    def visitorEmail(self, email, name):
        subject, from_email, to, reply_to = f'Thank you -{name}', EMAIL_FROM, email, owner_email
        html_content = render_to_string('email/msg.html', {'name': name})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to], reply_to=[reply_to])
        msg.attach_alternative(html_content, "text/html")
        return msg.send()


    
    def ownerEmail(self, msg, name, reply_to):
        subject, from_email, to = f'{name}-Enquiry', EMAIL_FROM, owner_email
        html_content = render_to_string('email/smsg.html', {'name': name, 'msg':msg})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to], reply_to=[reply_to])
        msg.attach_alternative(html_content, "text/html")
        return msg.send()