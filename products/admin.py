from django.contrib import admin
from .models import products
# Register your models here.
admin.site.register(products)
admin.site.site_header= "AWK"
admin.site.site_title= "AWK"