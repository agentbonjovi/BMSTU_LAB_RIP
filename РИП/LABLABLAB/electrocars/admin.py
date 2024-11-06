from django.contrib import admin

from electrocars import models

admin.site.register(models.Power_report)
admin.site.register(models.Station_report)
admin.site.register(models.Station)

# Register your models here.
