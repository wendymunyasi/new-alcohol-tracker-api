from django.urls import path
from . import views

urlpatterns = [
    # path('newsletter_recipients/'),
    path('', views.Recipients, name='index'),
]