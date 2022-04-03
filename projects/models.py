from django.db import models
from datetime import datetime

def current_time():
    now = datetime.now()
    time = now.strftime('%m.%d.%Y-')
    return time

def upload_location(instance, filename, **kwargs):
    file_path = 'projects/{project_name}/{timestamp}-{filename}'.format(
        project_name=str(instance.name), timestamp=current_time(), filename=filename
    )
    return file_path


class DoneProjects(models.Model):
    name                    = models.CharField(max_length=256, null=False, blank=False)
    body                    = models.TextField(max_length=5000, null=False, blank=False, default='this is default text')
    project_url             = models.URLField(max_length=200, null=False, blank=False, default='this is default text')
    id                      = models.AutoField(primary_key=True)
    thumbnail               = models.ImageField(upload_to=upload_location, null=False, blank=False, default='default.jpg') 
    frontend                = models.CharField(max_length=256, null=False, blank=False)
    backend                 = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'project'
        verbose_name_plural = 'Our Projects' 
