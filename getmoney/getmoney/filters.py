import django_filters as filters
from .models import Adv


class AdvFilter(filters.FilterSet):
    owner = filters.CharFilter(field_name='owner__username')
    class Meta:
        model = Adv
        fields = {
            'wn8': ['gt', 'lt'],
            'wins_percent': ['gt', 'lt'],
            'tag': ['icontains'],

        }
