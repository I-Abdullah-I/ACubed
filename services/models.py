from django.db import models

from datetime import datetime

def current_time():
    now = datetime.now()
    time = now.strftime('%m.%d.%Y-')
    return time

def upload_location(instance, filename, **kwargs):
    file_path = 'services/{service_name}/{timestamp}-{filename}'.format(
        service_name=str(instance.name), timestamp=current_time(), filename=filename
    )
    return file_path


class Services(models.Model):
    name                = models.CharField(max_length=50, null=False, blank=False)
    icon                = models.ImageField(upload_to=upload_location, null=False, blank=False)
    body                = models.CharField(max_length=256, null=False, blank=False)
    image               = models.ImageField(upload_to=upload_location, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'service'    
        verbose_name_plural = 'Our Services'    
    