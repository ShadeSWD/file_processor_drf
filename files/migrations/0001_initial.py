# Generated by Django 5.0.2 on 2024-02-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="files/", verbose_name="файл")),
                (
                    "upload_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата загрузки"
                    ),
                ),
                (
                    "processed",
                    models.BooleanField(default=False, verbose_name="статус обработки"),
                ),
            ],
            options={
                "verbose_name": "файл",
                "verbose_name_plural": "файлы",
            },
        ),
    ]