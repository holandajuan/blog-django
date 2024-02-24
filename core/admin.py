from django.contrib import admin
from .models import PostModel, Comment

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content')

    


