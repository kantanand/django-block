# coding: utf-8
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from community.storage import OverwriteStorage, logo_name


# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to=logo_name, storage=OverwriteStorage(), blank=True)
    link = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now = True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='community_modified_by')

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communitys'

    def __str__(self):
        return self.name