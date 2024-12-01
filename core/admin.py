from django.contrib import admin
from  . import  models
from solo.admin import SingletonModelAdmin
# Register your models here.
admin.site.register(models.Images)
admin.site.register(models.Contact, SingletonModelAdmin)