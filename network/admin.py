from django.contrib import admin

from .models import Follower, Post, User

# Register your models here.
admin.site.register(Follower)
admin.site.register(Post)
admin.site.register(User)
