from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    ptype = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, default=None)
    description = models.TextField()
    image = models.FileField(upload_to='files/')
    characteristic = models.JSONField()
    price = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    create_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
