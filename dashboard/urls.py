from django.urls import path
from . import views

urlpatterns =[
   path('short/', views.ShortenURL),
]