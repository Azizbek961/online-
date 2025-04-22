from django.contrib import admin
from .models import BLog, BlogComment

admin.site.register(BLog)
admin.site.register(BlogComment)