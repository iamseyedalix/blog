from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['subtitle', 'user', 'release_date', 'tag']


admin.site.register(Post, PostAdmin)