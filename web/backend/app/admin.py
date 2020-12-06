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
    filter_horizontal = ('files',)


class SimilarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'dataset_id')
    ordering = ('id', 'dataset_id')
    filter_horizontal = ('targets', 'results',)


admin.site.register(models.File, FileAdmin)
admin.site.register(models.Dataset, DatasetAdmin)
admin.site.register(models.Similarity, SimilarityAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
