from __future__ import unicode_literals

from django.db import models
from constants import CLIENTS, PRODUCT_AREAS

# Create your models here.
class FeatureRequest(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=2048)
    client = models.IntegerField(choices=CLIENTS)
    client_priority = models.IntegerField()
    target_date = models.DateField()
    ticket_url = models.CharField(max_length=2048)
    product_area = models.IntegerField(choices=PRODUCT_AREAS)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
