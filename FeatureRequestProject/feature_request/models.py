from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FeatureRequest(models.Model):
    # Available clients used in model
    CLIENTS = (
        (1, 'Client A'),
        (2, 'Client B'),
        (3, 'Client C'),
    )
    # Available product areas used in model
    PRODUCT_AREAS = (
        (1, 'Policies'),
        (2, 'Billing'),
        (3, 'Claims'),
        (4, 'Reports'),
    )
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=2048)
    client = models.IntegerField(choices=CLIENTS)
    client_priority = models.IntegerField()
    target_date = models.DateField()
    ticket_url = models.CharField(max_length=2048)
    product_area = models.IntegerField(choices=PRODUCT_AREAS)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
