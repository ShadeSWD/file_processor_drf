import os

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase


class FilesTestCase(APITestCase):

    def setUp(self):
        pass

    def test_post_files(self):
        response = self.client.get("/upload/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.post("/upload/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        file = SimpleUploadedFile(
            "test_file.txt", b"content", content_type="text/plain"
        )
        response = self.client.post("/upload/", {"file": file})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        os.remove("media/files/test_file.txt")

    def test_get_files(self):
        response = self.client.get("/files/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])
