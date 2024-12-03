from django.contrib import admin
from . import models
from solo.admin import SingletonModelAdmin


@admin.action(description="Deactivate selected images")
def deactivate_images(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.action(description="Activate selected images")
def activate_images(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.register(models.Images)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'active')
    actions = [deactivate_images, activate_images]


admin.site.register(models.Contact, SingletonModelAdmin)
