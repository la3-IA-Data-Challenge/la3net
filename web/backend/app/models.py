from django.db import models

import uuid
import os


class File(models.Model):
    file = models.FileField(
        upload_to="upload/", blank=False, null=False)


class Dataset(models.Model):
    files = models.ManyToManyField(File, verbose_name="Fichiers")
