from django.contrib import admin
from .models import Book, ActivityLog

# Register your models here.

admin.site.register(Book)
admin.site.register(ActivityLog)
