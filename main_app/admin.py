from django.contrib import admin
from .models import Shoe, Cleaning, Store

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Cleaning)
admin.site.register(Store)