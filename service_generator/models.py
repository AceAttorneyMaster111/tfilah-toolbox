from django.db import models

class Prayer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

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

class Song(models.Model):
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    chordsheet = models.FileField(upload_to="chordsheets/")
    # TODO: Ensure chordsheet file

    def __str__(self):
        return f"{self.title} ({self.artist})"

# TODO: Create model for Service, for saving services