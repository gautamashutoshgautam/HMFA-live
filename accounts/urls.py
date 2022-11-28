from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('register/', views.registerPage,name="register"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),


    path('', views.home,name="home"),
    path('user/', views.userPage, name="user-page"),

    path('artworks', views.artworks,name="artworks"),
    path('about', views.about,name="about"),
    
    path('arts/', views.arts, name = "arts"),
    path('create_arts/', views.createArts, name = "create_arts"),
    path('update_arts/<str:pk_test>/', views.updateArts, name ="update_arts"),
    path('delete_arts/<str:pk_test>/', views.deleteArts, name ="delete_arts"),

    path('create_exhibitions/', views.createExhibitions, name = "create_exhibitions"),
    path('update_exhibitions/<str:pk_test>/', views.updateExhibitions, name ="update_exhibitions"),
    path('delete_exhibitions/<str:pk_test>/', views.deleteExhibitions, name ="delete_exhibitions"),


    path('account/', views.accountSettings, name="account"),

    path('museum/', views.museum, name="museum"), 
    
    path('members/<str:pk>/', views.members, name="members"),
    path('ticket/', views.ticket,name="ticket"),
    path('create_bookings/<str:pk>/', views.createBookings, name ="create_bookings"),
    path('update_bookings/<str:pk_test>/', views.updateBookings, name ="update_bookings"),
    path('delete_bookings/<str:pk_test>/', views.deleteBookings, name ="delete_bookings"),
 ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)