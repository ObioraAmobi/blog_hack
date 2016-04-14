from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author is linked to a registered user in the auth_user table
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen
    tag = models.CharField(max_length=100, blank=True, null=True)
    # image = models.ImageField(upload_to="images", blank=True, null=True)
    # to use ImageField be sure to have installed the pillow imaging library


def publish(self):
    self.published_date = timezone.now()
    self.save()


def __str__(self):
    return self.title