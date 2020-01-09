import os
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def index(request):

    return render(request, 'hrag/index.html')

def about(request):
    
    return render(request, 'hrag/about.html')

def projects(request):

    return render(request, 'hrag/projects.html')

def contact(request):
    if request.method == 'GET':
        
        return render(request, 'hrag/contact.html')

    if request.method == "POST":

        name = request.POST['name']
        subject = request.POST['subject']
        senderEmail = request.POST['email']
        content = request.POST['message']

        message = Mail(
            from_email= str(senderEmail),
            to_emails='hragkara@gmail.com',
            subject=str(subject),
            html_content=str(content))
        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))



        return redirect('/contact')