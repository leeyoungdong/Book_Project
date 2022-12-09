# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BookTable(models.Model):
    level_0 = models.BigIntegerField(primary_key=True)
    index = models.BigIntegerField(blank=True, null=True)
    itemkey = models.ForeignKey('Reputation', models.DO_NOTHING, db_column='itemkey', blank=True, null=True)
    date = models.ForeignKey('Period', models.DO_NOTHING, db_column='date', blank=True, null=True)
    title = models.ForeignKey('Information', models.DO_NOTHING, db_column='title', blank=True, null=True)
    author = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'book_table'


class Buyc(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    portal = models.CharField(primary_key=True, max_length=700)
    accucnt = models.FloatField(blank=True, null=True)
    aggrcnt = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    sales = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'buyc'


class Information(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(primary_key=True, max_length=700)
    context = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'information'


class LibDate(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    pub = models.CharField(primary_key=True, max_length=700)
    pub_year = models.FloatField(blank=True, null=True)
    pub_month = models.FloatField(blank=True, null=True)
    pub_day = models.FloatField(blank=True, null=True)
    pub_date = models.FloatField(blank=True, null=True)
    repub = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_date'


class LibInformation(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    title = models.CharField(primary_key=True, max_length=700)
    isbn = models.TextField(blank=True, null=True)
    isbn_add_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_information'


class LibSA(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    a_key = models.CharField(primary_key=True, max_length=700)
    author = models.TextField(blank=True, null=True)
    ebook = models.TextField(blank=True, null=True)
    subject = models.TextField(db_column='SUBJECT', blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_s_a'


class LibTable(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    a_key = models.OneToOneField(LibSA, models.DO_NOTHING, db_column='a_key', primary_key=True)
    title = models.ForeignKey(LibInformation, models.DO_NOTHING, db_column='title', blank=True, null=True)
    pub = models.ForeignKey(LibDate, models.DO_NOTHING, db_column='pub', blank=True, null=True)
    author = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lib_table'


class Period(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    date = models.CharField(primary_key=True, max_length=700)
    year = models.BigIntegerField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)
    week = models.FloatField(blank=True, null=True)
    day = models.FloatField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'period'


class Reputation(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    itemkey = models.CharField(primary_key=True, max_length=700)
    rank = models.FloatField(blank=True, null=True)
    review_num = models.TextField(blank=True, null=True)
    review_rate = models.TextField(blank=True, null=True)
    portal = models.ForeignKey(Buyc, models.DO_NOTHING, db_column='portal', blank=True, null=True)
    new1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reputation'
