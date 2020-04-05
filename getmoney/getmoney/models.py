from django.db import models
from django.contrib.auth.models import User


class Adv(models.Model):
    PAYED = True
    NOT_PAYED = False
    STATUS = (
        (PAYED, 'Payed'),
        (NOT_PAYED, 'Not payed')
    )

    owner = models.ForeignKey('auth.User', related_name='ads', on_delete=models.CASCADE)

    datetime_start = models.DateTimeField(auto_now=True)
    datetime_end = models.DateTimeField()
    content = models.TextField(max_length=512)
    wn8 = models.IntegerField(default=0)
    wins_percent = models.IntegerField(default=0)
    tag = models.CharField(max_length=7, null=True)
    url_clan = models.CharField(max_length=150)
    status = models.BooleanField(max_length=10, choices=STATUS, default=NOT_PAYED)


class YandexPaymentModel(models.Model):
    operation_id = models.CharField(max_length=50)
    amount = models.FloatField()
    codepro = models.CharField(max_length=10)
    label = models.CharField(max_length=10)


class PrivatPaymentModel(models.Model):
    payment_id = models.CharField(max_length=50)
    state = models.CharField(max_length=1)
    message = models.CharField(max_length=200)
    amt = models.CharField(max_length=100)
    ccy = models.CharField(max_length=10)
