from rest_framework import serializers

from app import models


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ['id', 'file']

        extra_kwargs = {
            "file": {
                "read_only": False,
                "required": False,
            },
        }


class DatasetSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = models.Dataset
        fields = ['id', 'files']


class SimilaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Similarity
        fields = '__all__'


class SimilarityAllSerializer(serializers.ModelSerializer):
    dataset = DatasetSerializer()
    results = FileSerializer(many=True)
    targets = FileSerializer(many=True)

    class Meta:
        model = models.Similarity
        fields = 'id, dataset, targets, results'


class ExecuteSerializer(serializers.Serializer):
    similarityId = serializers.IntegerField()
    method = serializers.CharField()
