from django.contrib import admin

from portfolio.models import Project, PortfolioConfig


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'link']


@admin.register(PortfolioConfig)
class PortfolioConfigAdmin(admin.ModelAdmin):
    list_display = ['block', 'key', 'value']
