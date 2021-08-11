from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from hashirim_shelanu.models import Prayer, Song

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

class Service_Element(models.Model):
    class Element_Types(models.IntegerChoices):
        SONG = 1, "Song"
        PRAYER = 2, "Prayer"
        READING = 3, "Reading"
        IYUN = 4, "Iyun"
        OTHER = 5, "Other"

        @classmethod
        def get_limit_query(cls):
            limit = models.Q()
            for i, name in cls.choices:
                limit |= models.Q(app_label="service_generator", model=name + "_Element")
            return limit
    
    element_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=Element_Types.get_limit_query())
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey("element_type", "object_id")

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)
    element_list = models.ManyToManyField(Service_Element, through="Element_Position")

class Element_Position(models.Model):
    element = models.ForeignKey(Service_Element, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(unique=True)


class Song_Element(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE)

class Prayer_Element(models.Model):
    prayer = models.OneToOneField(Prayer, on_delete=models.CASCADE)

class Reading_Element(models.Model):
    pass

class Iyun_Element(models.Model):
    pass

class Other_Element(models.Model):
    pass