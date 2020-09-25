from django.contrib import admin
from django.urls import path, include
from .views import UserRegistertrationView

urlpatterns = [
    path('register/', UserRegistertrationView.as_view(), name='registration'),
]
