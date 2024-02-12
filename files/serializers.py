from rest_framework import serializers

from .models import File


class FileSerializerRetrieve(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["pk", "upload_at", "processed", "processed_at"]


class FileSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "file",
        ]
