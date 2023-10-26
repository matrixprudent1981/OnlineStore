from django.contrib import admin
from .models import Post, Comment, PostTest, Hashtag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostTest)
admin.site.register(Hashtag)


