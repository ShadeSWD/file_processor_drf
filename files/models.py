from django.db import models

NULLABLE = {"null": True, "blank": True}


class File(models.Model):
    file = models.FileField(verbose_name="файл", upload_to="files/")
    upload_at = models.DateTimeField(verbose_name="дата загрузки", auto_now_add=True)
    processed = models.BooleanField(verbose_name="статус обработки", default=False)
    processed_at = models.DateTimeField(verbose_name="время обработки", **NULLABLE)

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"
