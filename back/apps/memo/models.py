from django.db import models
from apps.user.models import MyUser


class Article(models.Model):
    title = models.CharField(max_length=30)
    article_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
