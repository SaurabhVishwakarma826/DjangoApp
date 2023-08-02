from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('',views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
    path('scrape_website/', views.scrape_website, name='scrape_website'),
]