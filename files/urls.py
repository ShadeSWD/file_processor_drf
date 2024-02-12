from django.urls import path

from .apps import FilesConfig
from .views import FileCreate, FileList, HomeView

app_name = FilesConfig.name

urlpatterns = [
    path("", HomeView.as_view()),
    path("upload/", FileCreate.as_view()),
    path("files/", FileList.as_view()),
]
