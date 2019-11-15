from django.db import models
from django.urls import reverse

class Link(models.Model):
    original_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    short_url = models.URLField(default=f'{id}')


    def __str__(self):
        return self.original_url


    def get_absolute_url(self):
        return reverse('short_link:link_detail', kwargs={'pk': self.pk})


    @staticmethod
    def short_url(url):
        link = Link.






