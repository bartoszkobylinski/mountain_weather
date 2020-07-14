from PIL import Image 
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='icon-user.png', upload_to='profile_picture')

    def __str__(self):
        return f"{self.user.username} profile"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='place_picture', blank=True)
    lat = models.DecimalField(default=0.0, decimal_places=6, max_digits=10)
    lon = models.DecimalField(default=0.0, decimal_places=6, max_digits=10)


    def __str__(self):
        return f" Post published {self.date} by {self.user.username}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk })

    def get_exif(self, image):
        image = Image.open(self.image)
        image.verify()
        return image._getexif()

    def get_geotagging(self, exif):
        if not exif:
            raise ValueError("No EXIF metadata found")

        geotagging = {}

        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                if idx not in exif:
                    return geotagging

                for (key, val) in GPSTAGS.items():
                    if key in exif[idx]:
                        geotagging[val] = exif[idx][key]

        return geotagging
    
    def get_decimal_from_dms(self, dms, ref):

        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2][0] / dms[2][1] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds

        return round(degrees + minutes + seconds, 5)

    def get_coordinates(self, geotags):
        lat = self.get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

        lon = self.get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

        return (lat,lon)


    def save(self, *args, **kwargs):
        if self.get_exif(self.image) is None:
            self.lat = 0
            self.lon = 0
        else:
            exif = self.get_exif(self.image)
            if self.get_geotagging(exif):
                geotags = self.get_geotagging(exif)
                coordinates = self.get_coordinates(geotags)
                lat = coordinates[0]
                lon = coordinates[1]
                self.lat = lat
                self.lon = lon
            else:
                self.lat = 0
                self.lon = 0
        super(Post, self).save(*args, **kwargs)