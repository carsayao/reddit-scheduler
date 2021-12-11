from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    #timezone

class Content(models.Model):
    default_title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.CharField(max_length=200)
    creation_date = models.DateTimeField()

class Post(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    override_title = models.CharField(max_length=300, blank=True)
    subreddit = models.CharField(max_length=200)
    strat = models.CharField(max_length=200)
    send_replies = models.BooleanField(null=False)
    flair = models.CharField(max_length=200, blank=True)
    reddit_link = models.URLField(blank=True)

class Strategy(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    strat_type = models.CharField(max_length=200)
    strat_date = models.DateTimeField(blank=True)