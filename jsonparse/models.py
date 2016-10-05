from django.db import models


class Group(models.Model):
    class Meta:
        db_table = 'group'
    group_region = models.CharField(max_length=100)


class Countries(models.Model):
    class Meta:
        db_table = 'country'
    country_name = models.CharField(max_length=100)
    country_value = models.FloatField()
    country_from = models.ForeignKey(Group)
