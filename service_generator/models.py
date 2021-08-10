from django.db import models

from hashirim_shelanu.models import Prayer

# Create your models here.

class Service_Type(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    prayers = models.ManyToManyField(Prayer, through="Prayer_Position")

    def __str__(self):
        return self.name

class Prayer_Position(models.Model):
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(unique=True)
    # TODO: Deal with the fact that this is ordered