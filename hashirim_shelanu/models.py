import io

from chopro import chopro2html
from django.core.validators import FileExtensionValidator
from django.db import models
from weasyprint import HTML, CSS


class PrayerTag(models.Model):
    name = models.SlugField(max_length=100)

    def __str__(self):
        return "#" + self.name


class Prayer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(PrayerTag, related_name="prayers")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="artists/", blank=True, null=True)

    def __str__(self):
        return self.name if self.name != "Unknown" else f"Unknown (ID {self.id})"


class SongTag(models.Model):
    name = models.SlugField(max_length=100)

    def __str__(self):
        return "#" + self.name


class Song(models.Model):
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    tags = models.ManyToManyField(SongTag, related_name="songs", blank=True)

    def __str__(self):
        return f"{self.title} ({self.artist})"


class ChordsheetContributor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Chordsheet(models.Model):
    file = models.FileField(upload_to="chordsheets/", validators=[FileExtensionValidator(["pro"])])
    contributors = models.ManyToManyField(ChordsheetContributor)
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)

    def get_pdf(self) -> io.BytesIO:
        buffer = io.BytesIO()

        self.file.open("r")
        chordsheet_html = HTML(string=chopro2html(self.file.read()) +
                               f"<div id=chordsheet-contributor>"
                               f"    <i>Contributed by {str(self.list_contributors)}</i>"
                               f"</div>")
        chordsheet_css = CSS(string="div.chords-lyrics-line {"
                             "   display: flex;"
                             "   font-family: Roboto Mono, monospace;"
                             "}"
                             "#chordsheet-contributor {"
                             "   padding-top: 10px;"
                             "}"
                             "div.chords:empty::before {"
                             "   content: ' ';"
                             "   white-space: pre;"
                             "}")
        self.file.close()

        chordsheet_html.write_pdf(buffer, stylesheets=[chordsheet_css])
        buffer.seek(0)
        return buffer

    @property
    def list_contributors(self) -> str:
        contributors: models.QuerySet[ChordsheetContributor] = self.contributors.all()
        if len(contributors) == 1:
            return str(contributors[0])
        if len(contributors) == 2:
            return str(contributors[0]) + " and " + str(contributors[1])
        contributor_strings: list[str] = [str(contributor) for contributor in contributors]
        contributor_strings[-1] = "and " + str(contributors[-1])
        return ", ".join(contributor_strings)
