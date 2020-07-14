
from PIL import Image 
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

# Create your tests here.
def get_exif(image):
        image = Image.open(image)
        image.verify()
        
        return image._getexif()

def get_geotagging(exif):
        if not exif:
            raise ValueError("No EXIF metadata found")

        geotagging = {}

        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                if idx not in exif:
                    geotagging.update(val=0)
                    return geotagging

                for (key, val) in GPSTAGS.items():
                    if key in exif[idx]:
                        geotagging[val] = exif[idx][key]
                  

        return geotagging

def get_decimal_from_dms(dms, ref):
    
        degrees = dms[0][0] / dms[0][1]
        minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2][0] / dms[2][1] / 3600.0

        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds

        return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)    


exif = get_exif('/home/bart/Desktop/zdjecia/744F8422-084D-45B8-B4B4-293BBCE5568D.JPG')
geotags = get_geotagging(exif)
print(geotags)  
coordinates = get_coordinates(geotags)
lat = coordinates[0]
lon = coordinates[1]


print(lat)
print(lon)