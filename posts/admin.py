from django.contrib import admin
from .models import PostModel,Comment

# Register your models here.
admin.site.register(PostModel)
admin.site.register(Comment)