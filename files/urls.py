from django.urls import path

from .apps import FilesConfig
from .views import FileCreate, FileList

app_name = FilesConfig.name

urlpatterns = [
    path("upload/", FileCreate.as_view()),
    path("files/", FileList.as_view()),
]
