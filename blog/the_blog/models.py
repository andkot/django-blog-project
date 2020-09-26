from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    creating_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} | {self.author}'

    def get_absolute_url(self):
        return reverse('article details', args=(str(self.id)))

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
