from django.contrib import admin
from .models import Adv, YandexPaymentModel, PrivatPaymentModel


admin.site.register(Adv)
admin.site.register(YandexPaymentModel)
admin.site.register(PrivatPaymentModel)