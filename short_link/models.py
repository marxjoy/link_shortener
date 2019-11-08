from django.db import models

class Link(models.Model):
    original_url = models.URLField()
    short_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

