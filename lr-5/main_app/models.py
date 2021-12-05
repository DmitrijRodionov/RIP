# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Building(models.Model):
    id_building = models.AutoField(db_column='ID_building', primary_key=True)  # Field name made lowercase.
    building_name = models.CharField(db_column='Building_name', max_length=100, blank=True, null=False)  # Field name made lowercase.
    descript = models.CharField(db_column='Descript', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    creation_year = models.IntegerField(db_column='Creation_year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Building'


class City(models.Model):
    id_city = models.AutoField(db_column='ID_city', primary_key=True)  # Field name made lowercase.
    city_name = models.CharField(db_column='City_name', max_length=100, blank=True, null=False)  # Field name made lowercase.
    descript = models.CharField(db_column='Descript', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_building = models.ForeignKey('Building', models.DO_NOTHING, db_column='ID_building', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'City'