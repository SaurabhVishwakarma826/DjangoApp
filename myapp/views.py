from django.shortcuts import render
from django.core.mail import send_mail
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'index.html')

def send_email(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        recipient = request.POST['recipient']
        subject = request.POST['subject']
        body = request.POST['body']

        send_mail(subject, body, sender, [recipient])
        return render(request, 'email_sent.html', {'recipient': recipient})
    else:
        return render(request, 'send_email.html')

def scrape_website(request):
    if request.method == 'POST':
        url = request.POST['url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()

        return render(request, 'scraped_website.html', {'content': content})
    else:
        return render(request, 'scrape_website.html')

