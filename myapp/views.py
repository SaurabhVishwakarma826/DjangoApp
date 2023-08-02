# email_sender/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')

def send_email(request):
    if request.method == 'POST':
        to_email = request.POST.get('to')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, message, from_email, [to_email])
            return render(request, 'index.html', {'msg':'Successfully send'})
        except Exception as e:
            return render(request, 'index.html', {'msg': str(e)})
    else:
        return render(request, 'index.html')


def scrape_website(request):
    if request.method == 'POST':
        url = request.POST['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()

        return render(request, 'scrape_website.html', {'content': content})
    else:
        return render(request, 'scrape_website.html')