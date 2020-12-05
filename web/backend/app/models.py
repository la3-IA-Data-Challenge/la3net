from django.db import models

import uuid
import os


class File(models.Model):
    file = models.FileField(
        upload_to="upload/", blank=False, null=False)


class Dataset(models.Model):
    files = models.ManyToManyField(File, verbose_name="Fichiers")


class PdfLinks(models.Model):
    pdf = models.ForeignKey(
        File, on_delete=models.DO_NOTHING, verbose_name="PDF", related_name="pdf")
    images = models.ManyToManyField(
        File, verbose_name="Images", related_name="images")


class Similarity(models.Model):
    dataset = models.ForeignKey(
        Dataset, verbose_name="Dataset", blank=False, null=False, on_delete=models.DO_NOTHING)
    targets = models.ManyToManyField(
        File, verbose_name="Cibles", related_name="targets")
    results = models.ManyToManyField(
        File, verbose_name="Résultat", related_name="results")
