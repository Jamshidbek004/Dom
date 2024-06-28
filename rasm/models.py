from django.db import models


# Create your models here.


class ImageKirish(models.Model):
    object = None
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ImagemMaket(models.Model):
    object = None
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ImagemOrqafon(models.Model):
    object = None
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ImagemMatn(models.Model):
    object = None
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class House(models.Model):
    title = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='house_images/')

    def __str__(self):
        return self.title


class Video(models.Model):
    object = None
    title = models.CharField(max_length=100)
    video_url = models.URLField(blank=True, null=True)
    text = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class NashiUslugi(models.Model):
    object = None
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class HouseDesign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video_url = models.URLField(blank=True, null=True)
    additional_features = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact2(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name

