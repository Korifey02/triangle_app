from django.db import models


class Triangle(models.Model):
    first_side = models.FloatField('Первый катет')
    second_side = models.FloatField('Второй катет')
