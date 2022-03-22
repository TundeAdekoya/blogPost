from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .managers import PublishedManager



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now, )
    created = models.DateTimeField(auto_now_add=True, )
    updated = models.DateTimeField(auto_now=True, )
    objects = models.Manager()
    published = PublishedManager() 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:postdetail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])




