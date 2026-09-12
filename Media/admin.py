from django.contrib import admin

from Media.models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','published_at','vercel_url')


