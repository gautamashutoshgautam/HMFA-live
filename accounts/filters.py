import django_filters
from django_filters import DateFilter
from .models import *


class BookingsFilter(django_filters.FilterSet):
    start_date= DateFilter(field_name="date_booked", lookup_expr='gte')
    end_date= DateFilter(field_name="date_booked", lookup_expr='lte')
    class Meta:     
        model = Bookings
        fields= '__all__' 
        exclude = ['member', 'date_booked']

class ArtsFilter(django_filters.FilterSet):
    class Meta:     
        model = Arts
        fields= '__all__' 
        exclude = ['art_on_loan', 'date_aquired', 'art_piece_id']

class ExhibitionsFilter(django_filters.FilterSet):
    class Meta:     
        model = Exhibitions
        fields= '__all__' 
        
