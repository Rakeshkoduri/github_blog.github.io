from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *


# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    product = models.CharField(max_length=1000,null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    post = models.ForeignKey(BlogModel, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
