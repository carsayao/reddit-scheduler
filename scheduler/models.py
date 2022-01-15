import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    #timezone
    def __str__(self):
        return self.username

class Content(models.Model):
    CONTENT_TYPES = [
        ('LINK',  'Link'),
        ('TEXT',  'Text'),
        ('MEDIA', 'Media'),
    ]
    # Unverified accounts, max=150
    default_title = models.CharField(max_length=300)
    kind = models.CharField(max_length=5, choices=CONTENT_TYPES, default='LINK')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.default_title
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
    # Method to tell Django how to calculate the canonical URL for an object. 
    # https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.get_absolute_url
    def get_absolute_url(self):
        return reverse('content-detail', kwargs={'pk': self.pk})

class Post(models.Model):
    POST_STRATEGY = [
        ('NOW',    'Now'),
        ('CUSTOM', 'Custom'),
    ]
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    override_title = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subreddit = models.CharField(max_length=200)
    strat = models.CharField(max_length=200)
    send_replies = models.BooleanField(null=False)
    flair = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=9999, blank=True)
    nsfw = models.BooleanField(null=False, default=False)

    strategy = models.CharField(max_length=6, choices=POST_STRATEGY, default='CUSTOM')
    scheduled_for = models.DateTimeField(blank=True, null=True)
    posted_at = models.DateTimeField(blank=True, null=True)
    reddit_link = models.URLField(blank=True)

    def __str__(self):
        return self.override_title

# class Strategy(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.strat_type