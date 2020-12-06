from .models import File, Dataset, Similarity
from .serializers import DatasetSerializer, FileSerializer, SimilaritySerializer, SimilarityAllSerializer, ExecuteSerializer

from django.conf import settings

from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .core.pipeline import method1, method2, method3

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

                targets_str = []
                for target in targets:
                    targets_str.append(
                        os.path.join(settings.MEDIA_ROOT, str(target.file))
                    )

                dataset_files_str = []
                for dataset_file in dataset_files:
                    dataset_files_str.append(
                        os.path.join(settings.MEDIA_ROOT,
                                     str(dataset_file.file))
                    )
                dataset_files_str.sort()

                if (method == "CNN"):
                    results_str = method1(
                        targets_str, dataset_files_str, feature_path)
                elif (method == "Hashing method"):
                    results_str = method2(
                        targets_str, dataset_files_str, feature_path)
                elif (method == "OBR Descriptor"):
                    results_str = method3(
                        targets_str, dataset_files_str, feature_path)
                else:
                    return Response({"Error 400": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

                for item in results_str:
                    filename = item.split("/")[-1]
                    f = File.objects.get(file__contains=filename)
                    sim.results.add(f)
                sim.save()

                sim_ser = SimilarityAllSerializer(sim)

                return Response(sim_ser.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("ERROR")
            print(e)
            return Response({"Error 500": "Internal serveur error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
