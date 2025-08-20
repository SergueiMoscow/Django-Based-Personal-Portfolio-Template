from django.contrib import admin

from portfolio.models import Project, PortfolioConfig, ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_github', 'featured', 'order')
    list_editable = ('is_github', 'featured', 'order')
    list_display_links = ('title',)
    search_fields = ('title', 'description')


@admin.register(PortfolioConfig)
class PortfolioConfigAdmin(admin.ModelAdmin):
    list_display = ['block', 'key', 'value']


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image_tag', 'caption', 'order')
    list_editable = ('order',)
    readonly_fields = ('image_tag',)
    list_filter = ('project',)