import datetime
import time

from celery import shared_task

from .models import File


@shared_task
def process_file(pk):
    file = File.objects.get(pk=pk)
    file_processing_imitator()
    file.processed = True
    file.processed_at = datetime.datetime.now()
    file.save()
    return {"file": file.pk, "processed": file.processed}


def file_processing_imitator():
    time.sleep(15)
