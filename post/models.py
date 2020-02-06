from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, default='')
    abstract = models.TextField(max_length=200, default='')
    content = RichTextField()
    author = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='post_image', blank=True)
    publish = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class AdminProfile(models.Model):
	username = models.OneToOneField(User, on_delete=models.DO_NOTHING)
	avatar = models.ImageField(upload_to='profile_avatar', blank=True)
	cover = models.ImageField(upload_to='profile_cover', blank=True)
	first_name = models.CharField(max_length=30, default='')
	last_name = models.CharField(max_length=40, default='')
	bio = models.TextField(max_length=150, default='', blank=True)
	city = models.CharField(max_length=15, default='', blank=True)
	website = models.URLField(default='', blank=True)
	github = models.URLField(default='', blank=True)
	twitter = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)

	def __str__(self):
		return "%s\t| %s"%(self.username, self.first_name +' '+ self.last_name)
