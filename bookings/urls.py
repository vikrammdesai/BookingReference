from django.urls import path
from .views import BookingListCreate

urlpatterns = [
    path('bookings/', BookingListCreate.as_view(), name='bookings'),
]