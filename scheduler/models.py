import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    #timezone
    def __str__(self):
        return self.username
        # return f'{self.username} id:{self.id}'

class Content(models.Model):
    # Unverified accounts, max=150
    default_title = models.CharField(max_length=300)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # link, text, media
    kind = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    def __str__(self):
        return self.default_title
        # return f'{self.default_title} id:{self.id} u_id:{self.user_id}'
    def was_published_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)

class Post(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    override_title = models.CharField(max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subreddit = models.CharField(max_length=200)
    strat = models.CharField(max_length=200)
    send_replies = models.BooleanField(null=False)
    flair = models.CharField(max_length=200, blank=True)
    reddit_link = models.URLField(blank=True)
    def __str__(self):
        return self.override_title
        # return self.override_title, self.subreddit, self.strat

class Strategy(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # now, custom
    strat_type = models.CharField(max_length=200)
    strat_date = models.DateTimeField(blank=True)
    def __str__(self):
        return self.strat_type