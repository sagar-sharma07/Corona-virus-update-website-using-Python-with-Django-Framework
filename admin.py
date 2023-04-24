from django.contrib import admin
from myapp import models

# Register your models here.

admin.site.register(models.contact)
admin.site.register(models.blog)
admin.site.register(models.registeruser)