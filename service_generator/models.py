from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.constraints import Deferrable, UniqueConstraint

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
    class Meta:
        ordering = ["index"]
        # TODO: Switch to PostgreSQL, which supports this
        # constraints = [UniqueConstraint(
        #     name="prayer_unique_index",
        #     fields=["index"],
        #     deferrable=Deferrable.DEFERRED
        # )]

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

    class Meta:
        ordering = ["index"]
        # constraints = [UniqueConstraint(
        #     name="element_unique_index",
        #     fields=["index"],
        #     deferrable=Deferrable.DEFERRED
        # )]


class Generic_Element(models.Model):
    class Meta:
        abstract = True

class Song_Element(Generic_Element, Song):
    class Meta(Generic_Element.Meta):
        proxy = True

class Prayer_Element(Generic_Element, Prayer):
    class Meta(Generic_Element.Meta):
        proxy = True

class Reading_Element(Generic_Element):
    pass

class Iyun_Element(Generic_Element):
    pass

class Other_Element(Generic_Element):
    pass