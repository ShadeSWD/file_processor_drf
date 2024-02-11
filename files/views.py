from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializerCreate, FileSerializerRetrieve


class FileCreate(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializerCreate
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        return serializer.save()

    @swagger_auto_schema()
    @action(detail=False, methods=["post"])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        instance_serializer = FileSerializerRetrieve(instance)
        return Response(instance_serializer.data)
