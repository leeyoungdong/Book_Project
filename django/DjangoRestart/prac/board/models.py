# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Context(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    news_publisher = models.TextField(blank=True, null=True)
    word_one = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'context'


class Date(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    day = models.BigIntegerField(blank=True, null=True)
    index = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'date'




class NewsTable(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    index = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'news_table'
