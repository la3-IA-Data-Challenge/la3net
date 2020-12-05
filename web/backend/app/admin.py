from django.contrib.auth.models import User, Group
from django.contrib import admin
from app import models

# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file')
    ordering = ('id', )


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ('id', )


admin.site.register(models.File, FileAdmin)
admin.site.register(models.Dataset, DatasetAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
