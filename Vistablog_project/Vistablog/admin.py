from django.contrib import admin
from .models import *

# Register your models here.

# Index 
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'description',)
    # fields = ['name', 'description', 'image']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('title', 'category','post_image_des', 'date',)
    # fields = ['category', 'title', 'post_image', 'content', 'content_video']


# About 
admin.site.register([Mission,Profile, Acknowledgement])

@admin.register(Review_message)
class Review_messageAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name', 'email','message','date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('commenter','post', 'date', 'body')