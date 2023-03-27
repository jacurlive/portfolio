from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.models import About, Skill, Sumary, Education, Category, Project, Image, Message


@admin.register(About)
class AboutAdmin(ModelAdmin):
    fields = ('image', 'phone', 'city', 'age', 'degree', 'email', 'description', 'instagram_link', 'twitter_link',
              'linkedin_link')
    list_display = ('id', 'full_name', 'degree', 'email')


@admin.register(Skill)
class SkillsAdmin(ModelAdmin):
    fields = ('name', 'percent')
    list_display = ('name', 'percent')


@admin.register(Sumary)
class SumaryAdmin(ModelAdmin):
    fields = ('description',)
    list_display = ('full_name', 'city', 'phone', 'email')


@admin.register(Education)
class EducationAdmin(ModelAdmin):
    fields = ('title', 'year', 'place', 'description')
    list_display = ('title', 'place')


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    fields = ('title', 'description', 'category', 'client', 'pic', 'url')
    list_display = ('title', 'category', 'client', 'url', 'image_tag')
    readonly_fields = ('image_tag',)


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    fields = ('image', 'project')


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'answered')
    list_display_links = ('id', 'name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('answered',)
    list_filter = ('answered', 'date')
    readonly_fields = ('name', 'email', 'subject', 'message')
