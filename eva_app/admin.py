from django.contrib import admin

from eva_app import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Publisher)