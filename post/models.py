from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, default="")
    summary = models.TextField(max_length=300, default="")
    content = models.TextField(default="")
    author = models.CharField(default="Ali Reza Yahyapour", max_length=50)
    publish = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
