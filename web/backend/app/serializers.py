from rest_framework import serializers

from app import models


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ['id', 'file']


class DatasetSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = models.Dataset
        fields = ['id', 'files']
