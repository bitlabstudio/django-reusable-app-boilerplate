from django.db import models


class Example(models.Model):
    text = models.TextField(blank=True, null=True)

