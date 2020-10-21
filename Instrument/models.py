import uuid
import os
from django.db import models
from rest_framework.reverse import reverse


def instrument_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]  # Get the extension.
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/instrument/', filename)


# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return "/sections/%i/" % self.id
        #return reverse('section', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=100)
    invention_date = models.DateField()
    image = models.ImageField(null=True, upload_to=instrument_image_file_path)
    section = models.ForeignKey(Section, related_name='instruments',
                                on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('instrument-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
