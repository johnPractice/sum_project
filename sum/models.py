from typing import Iterable, Optional
from django.db import models
from django.db.models import Sum
# Create your models here.


class SumNumber(models.Model):
    number1 = models.IntegerField(null=False, blank=False)
    number2 = models.IntegerField(null=False, blank=False)
    total_number = models.IntegerField(null=False, blank=False, default=0)

    @staticmethod
    def get_total_vlaue():
        return SumNumber.objects.all().aggregate(Sum('total_number'))
