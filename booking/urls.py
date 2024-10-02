# urls.py
from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('appointment_success/', views.appointment_success_view,
         name='appointment_success'),
]
