from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class LaptopProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    description = models.TextField()
    image = models.FileField(upload_to='files/')
    cpu = models.CharField(max_length=128)
    gpu = models.CharField(max_length=128)
    ram = models.CharField(max_length=128)
    memory = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    create_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
