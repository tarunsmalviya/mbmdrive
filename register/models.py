from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, primary_key=True)
    mobile = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=1, default='S', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()
