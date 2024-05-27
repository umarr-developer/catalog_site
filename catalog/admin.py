from django.contrib import admin

from catalog.models import Brand, LaptopProduct, PhoneProduct, AccessoriesProduct

# Register your models here.
admin.site.register(Brand)
admin.site.register(LaptopProduct)
admin.site.register(PhoneProduct)
admin.site.register(AccessoriesProduct)
