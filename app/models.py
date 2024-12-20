from django.db import models

class Folio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='app/images/')
    url = models.URLField(blank=True)