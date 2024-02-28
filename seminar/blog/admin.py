from django.contrib import admin
from .models import Autor, Post, Comment


admin.site.register(Autor)
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

# Register your models here.
