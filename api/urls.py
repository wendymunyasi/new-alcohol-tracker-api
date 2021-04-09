from django.urls import path
from . import views

urlpatterns = [
    path('newsletter_recipients1/', views.Recipients, name='recipients'),
    path('newsletter_recipients2/', views.NewsletterRecipientsListView.as_view(), name='recipients2'),
    path('new_recipient/', views.NewsletterRecipientCreateView.as_view(), name='recipient-create'),
]




