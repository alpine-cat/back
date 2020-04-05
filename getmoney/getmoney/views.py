from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AdvSerializer, UserSerializer, TokenSerializer, PrivatSerializer, YandexSerializer
from .models import Adv, PrivatPaymentModel, YandexPaymentModel
from django.contrib.auth.models import User
from rest_framework_simplejwt import views as jwt_views
from rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.models import TokenUser
from .filters import AdvFilter
from rest_framework.pagination import LimitOffsetPagination
import datetime

class CustomAccessTokenView(jwt_views.TokenObtainPairView):
    serializer_class = TokenSerializer


class AdvViewSet(viewsets.ModelViewSet):
    queryset = Adv.objects.filter(status=True)
    serializer_class = AdvSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_class = AdvFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotPayedViewSet(viewsets.ModelViewSet):
    queryset = Adv.objects.filter(status=False)
    serializer_class = AdvSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PrivatPaymentViewSet(viewsets.ModelViewSet):
    queryset = PrivatPaymentModel.objects.all()
    serializer_class = PrivatSerializer


class YandexPaymentViewSet(viewsets.ModelViewSet):
    queryset = YandexPaymentModel.objects.all()
    serializer_class = YandexSerializer

    def create(self, request, *args, **kwargs):
        context = super(YandexPaymentViewSet, self).create(request, *args, **kwargs)
        try:
            if request.data['codepro'] == 'true':
                pass
            else:
                adv = Adv.objects.get(status=False, id=int(request.data['label']))
                if adv:
                    adv.status = True
                    adv.save()
        finally:
            pass
        return context


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class MyRegisterView(RegisterView):
    token_model = TokenUser

    def get_response_data(self, user):
        refresh = TokenSerializer.get_token(user)
        data = dict()

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = {"pk": refresh.user.pk,
                        "username": str(refresh.user.username),
                        "email": str(refresh.user.email),
                        "first_name": str(refresh.user.first_name),
                        "last_name": str(refresh.user.last_name)
                        }

        return data

