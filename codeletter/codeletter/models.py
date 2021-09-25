from django.db import models
from django.contrib.auth.models import User

class Concept(models.Model):
    concept_id = models.CharField(max_length = 10, primary_key=True)
    concept_name = models.CharField(max_length=100)

class UserPreference(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    concept_id = models.ForeignKey(Concept, on_delete=models.CASCADE)

class Article(models.Model):
    article_id = models.CharField(max_length = 10, primary_key=True)
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    concept = models.CharField(max_length=100)
    doi = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank = True)

class SentArticle(models.Model):
    sent_article_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(auto_now_add=True)
    concept_id = models.ForeignKey(Concept, on_delete=models.CASCADE)
    read_flag = models.BooleanField(default=False)

class UserBadge(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    concept_id = models.ForeignKey(Concept, on_delete=models.CASCADE)
    user_badge = models.CharField(max_length=50, choices = [('Beginner','Beginner'),('Intermediate','Intermediate'),('Expert','Expert')], default='Beginner')