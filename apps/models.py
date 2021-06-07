from django.db import models


# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=3, default='')
    num = models.CharField(max_length=10, default='')
    mail = models.CharField(max_length=50, default='')

    class Meta:
        db_table = "data"
