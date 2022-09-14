from django.contrib import admin
from .models import Contact, Subscriber, Post, Comment
from technicalfirst import models

# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = (
        'Name',
        'subject',
    )
    search_fields = ('Name', 'subject',)

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = (
        'post_id',
        'comment_name',
        'comment_date',
    )
    search_fields = ('comment_name',)

@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):
    list_display = (
        'id',
        'Name',
        'Email',
    )
    search_fields = ('Name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'post_key',
        'post_category',
        'post_title',
        'date',
    )
    search_fields = ('post_title',)