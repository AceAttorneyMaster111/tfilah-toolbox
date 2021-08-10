import io

from chopro import chopro2html

from django.db import models

from weasyprint import HTML, CSS

class Prayer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name if self.name != "Unknown" else f"Unknown (ID {self.id})"

class Song(models.Model):
    prayer = models.ForeignKey(Prayer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    # TODO: Ensure chordsheet file

    def __str__(self):
        return f"{self.title} ({self.artist})"

class Chordsheet_Contributor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chordsheet(models.Model):
    file = models.FileField(upload_to="chordsheets/")
    contributors = models.ManyToManyField(Chordsheet_Contributor)
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)

    def get_pdf(self):
        buffer = io.BytesIO()

        self.file.open("r")
        chordsheet_html = HTML(string=chopro2html(self.file.read()) +
        "<div id=chordsheet-contributor>"
            "<i>Contributed by " + str(self.list_contributors) +
        "</div>")
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
    def list_contributors(self):
        contributors = self.contributors.all()
        if len(contributors) == 1:
            return contributors[0]
        if len(contributors) == 2:
            return contributors[0] + " and " + contributors[1]
        contributors[-1] = "and " + contributors[-1]
        return ", ".join(contributors)

# TODO: Create model for Service, for saving services