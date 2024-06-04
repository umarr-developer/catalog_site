from django.contrib import admin

from catalog.models import Brand, Product, ProductType

# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductType)