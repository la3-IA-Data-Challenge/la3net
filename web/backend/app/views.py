from .models import File, Dataset, Similarity
from .serializers import DatasetSerializer, FileSerializer, SimilaritySerializer, SimilarityAllSerializer, ExecuteSerializer

from django.conf import settings

from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

import os

# Create your views here.


class DatasetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DatasetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class FileList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FileDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SimilarityList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Similarity.objects.all()
    serializer_class = SimilaritySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SimilarityDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Similarity.objects.all()
    serializer_class = SimilarityAllSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class Execute(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = ExecuteSerializer(data=request.data)

            if serializer.is_valid():
                sim = Similarity.objects.get(
                    id=serializer.validated_data['similarityId'])

                method = serializer.validated_data['method']

                targets = sim.targets.all()
                dataset_files = sim.dataset.files.all()

                if sim.dataset.id == 1:
                    feature_path = os.path.join(
                        settings.MEDIA_ROOT, "features_mn.pkl")
                else:
                    feature_path = ""

                for i in range(0, 10):
                    f = dataset_files[i]
                    path = os.path.join(settings.MEDIA_ROOT, str(f.file))
                    print(path)

                # TODO : Exécuter le modèle
                # TODO : rename methods - backend
                if (method == "method1"):
                    pass
                elif (method == "method2"):
                    pass
                elif (method == "method3"):
                    pass
                else:
                    return Response({"Error 400": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

                # List of File
                sim_files = []
                for item in sim_files:
                    sim.results.add(item)
                sim.save()

                sim_ser = SimilarityAllSerializer(sim)

                return Response(sim_ser.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response({"Error 500": "Internal serveur error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
