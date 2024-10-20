from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.MenuView.as_view(), name="menu"),
    path('menu_item/<int:pk>/', views.MenuItemView.as_view(), name="menu_item"),  
    path('bookings/', views.bookings, name='bookings'), 
    path('restaurant/booking/', include(router.urls)),
    path('obtain-auth-token/', obtain_auth_token),
]