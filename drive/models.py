from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

import os


def path_and_rename(instance, filename):
    upload_to = 'drive'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(str(DriveFile.objects.count() + 1), ext)

    return os.path.join(upload_to, filename)


class DriveFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    file = models.FileField(upload_to=path_and_rename)

    def __str__(self):
        return self.user.get_full_name() + ' -> ' + self.name
