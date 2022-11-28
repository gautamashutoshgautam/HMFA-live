from django.urls import path
from reports import views
# Create your views here.

urlpatterns = [
    path('',views.reports,name='reports'),
    path('report_art/',views.report_art,name='report_art'),
    path('report_bookings/', views.report_bookings, name='report_bookings'),
    path('report_exhibitions/', views.report_exhibitions,name='report_exhibitions'),
]