from dataclasses import dataclass
from distutils.command.upload import upload
from statistics import mode
from django.db import models
from ckeditor.fields import RichTextField

# Contacts models
class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=150)
    messages = models.TextField()

# Subscriber Model
class Subscriber(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50, unique=True)
    date = models.DateField(auto_now=True)

# Comment
class Comment(models.Model):
    post_id = models.IntegerField()
    comment_name = models.CharField(max_length=30)
    comment_msg = models.CharField(max_length=250)
    comment_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"

# All Post Model
class Post(models.Model):
    post_key = models.AutoField(primary_key=True)
    post_category = models.CharField(max_length=50)
    post_subtitle = RichTextField(null=True, blank=False)
    post_title = models.CharField(max_length=255)
    thumbnail_img = models.ImageField(upload_to='pic')
    desc1 = RichTextField(null=True, blank=False)
    post_img2 = models.ImageField(upload_to='pic')
    desc2 = RichTextField(null=True, blank=False)
    post_slug = models.SlugField(null=False, unique=True)
    date = models.DateField(auto_now=True)
    



