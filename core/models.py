from django.db import models

# Create your models here.

class TwPatchNote(models.Model):
    version = models.CharField(max_length=45)
    note = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'TW_PATCH_NOTE'
        
        

class TwCafe(models.Model):
    cafe_name = models.CharField(max_length=200)
    location = models.CharField(max_length=50, blank=True, null=True)
    tables = models.CharField(max_length=50, blank=True, null=True)
    snack = models.CharField(max_length=100, blank=True, null=True)
    toilet = models.CharField(max_length=100, blank=True, null=True)
    cafe_size = models.CharField(max_length=45, blank=True, null=True)
    power_socket = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    ice_coffee = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TW_CAFE'


