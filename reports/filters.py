import django_filters

from .models import * 

class ExhibitionsFilter(django_filters.FilterSet):
    class Meta:
        model = Exhibitions
        fields = ['exhibition_year']