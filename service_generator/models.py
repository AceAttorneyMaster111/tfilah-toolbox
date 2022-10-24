from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
# from django.db.models.constraints import Deferrable, UniqueConstraint

from hashirim_shelanu.models import Prayer, Song

# Create your models here.


class ServiceType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    prayers = models.ManyToManyField(Prayer, through="PrayerPosition")

    def __str__(self):
        return self.name


class PrayerPosition(models.Model):
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        ordering = ["index"]
        # TODO: Switch to PostgreSQL, which supports this
        # constraints = [UniqueConstraint(
        #     name="prayer_unique_index",
        #     fields=["index"],
        #     deferrable=Deferrable.DEFERRED
        # )]


class ServiceElement(models.Model):
    class ElementTypes(models.IntegerChoices):
        SONG = 1, "Song"
        PRAYER = 2, "Prayer"
        READING = 3, "Reading"
        IYUN = 4, "Iyun"
        OTHER = 5, "Other"

        @classmethod
        def get_limit_query(cls) -> models.Q:
            limit = models.Q()
            for _, name in cls.choices:
                limit |= models.Q(app_label="service_generator", model=name + "_Element")
            return limit
    
    element_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=ElementTypes.get_limit_query()
    )
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey("element_type", "object_id")
    point = models.CharField(max_length=200)
    supporting = None

# ********************************
# ****** REMOVED FROM SPEC *******
# ********************************
# class Service(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     service_type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)
#     element_list = models.ManyToManyField(Service_Element, through="Element_Position")

# class ElementPosition(models.Model):
#     element = models.ForeignKey(Service_Element, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     index = models.PositiveSmallIntegerField(unique=True)

#     class Meta:
#         ordering = ["index"]
#         # constraints = [UniqueConstraint(
#         #     name="element_unique_index",
#         #     fields=["index"],
#         #     deferrable=Deferrable.DEFERRED
#         # )]


class GenericElement(models.Model):
    def get_short_name(self) -> str:
        raise NotImplementedError("Cannot run abstract method")

    def __str__(self):
        return self.get_short_name()
    
    class Meta:
        abstract = True


class SongElement(GenericElement, Song):
    def get_short_name(self) -> str:
        return self.title
    
    class Meta(GenericElement.Meta):
        proxy = True


class PrayerElement(GenericElement, Prayer):
    def get_short_name(self) -> str:
        return self.name
    
    class Meta(GenericElement.Meta):
        proxy = True


class ReadingElement(GenericElement):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)

    def get_short_name(self) -> str:
        return self.title


class IyunElement(GenericElement):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def get_short_name(self) -> str:
        return self.title


class OtherElement(GenericElement):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def get_short_name(self) -> str:
        return self.title
