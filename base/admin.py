from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Business)
admin.site.register(models.NeighbourHood)
admin.site.register(models.Post)