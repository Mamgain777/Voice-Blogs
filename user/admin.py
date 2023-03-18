from django.contrib import admin
from user.models import Blog, Comment, Category, UserProfile
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(UserProfile)