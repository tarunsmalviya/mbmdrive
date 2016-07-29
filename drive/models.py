from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import os
from uuid import uuid4


class Branch(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    abbreviation = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    abbreviation = models.CharField(max_length=10, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(Book.objects.count() + 1, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Book(models.Model):
    file = models.FileField(upload_to=path_and_rename)
    author = models.CharField(max_length=150, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)


class BookRelation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Paper(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False)
    year = models.PositiveSmallIntegerField(null=False)


class Notification(models.Model):
    message = models.CharField(max_length=500, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
