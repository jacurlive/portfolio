from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.models import About


@admin.register(About)
class AboutAdmin(ModelAdmin):
    fields = ('image', 'phone', 'city', 'age', 'degree', 'email', 'description')
    list_display = ('id', 'full_name', 'degree', 'email')
