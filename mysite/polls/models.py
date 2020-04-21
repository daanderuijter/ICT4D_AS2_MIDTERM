import datetime
import requests

from django.db import models
from django.utils import timezone
from django.db.models import F, Count

class Topic(models.Model):
    topic_text = models.CharField(max_length=200)
    question_count = models.IntegerField(default=0)

    def __str__(self):
        return self.topic_text
    
    def get_wikipedia_article(self):
        url = "None"
        r = requests.get("https://en.wikipedia.org/wiki/" + str(self.topic_text))
        if r.status_code == 200:
            url = r.url
        return url
    get_wikipedia_article.short_description = 'Wiki Page'

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text