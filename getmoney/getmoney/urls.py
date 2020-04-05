from rest_framework import routers
from .views import AdvViewSet, UserViewSet, NotPayedViewSet, YandexPaymentViewSet, PrivatPaymentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'advertisements', AdvViewSet)
router.register(r'not-payed', NotPayedViewSet)
router.register(r'yandex-response', YandexPaymentViewSet)
router.register(r'privat-response', PrivatPaymentViewSet)
