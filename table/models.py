from django.db import models

class DataRow(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)
    column3 = models.CharField(max_length=255)
    column4 = models.CharField(max_length=255)
    column5 = models.CharField(max_length=255)
