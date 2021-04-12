from django.shortcuts import redirect, render
from .settings import EMAIL_FROM
from django.core.mail import EmailMultiAlternatives, message
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .send_email import *
from django.contrib import messages

sendEmail = Email()



def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']

        sendEmail.visitorEmail(email, name)
        sendEmail.ownerEmail(comment, name, email)
        messages.success(request, "Message Sent")
        return redirect('/')
    else:
        return render(request, 'index.html')