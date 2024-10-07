from django.urls import path
from . import views
from .views import ServicesDetails
app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients, name='clients'),

    path('services/', views.services, name='services'),
    path('FAQ/', views.faq, name='faq'),
    path('services/<str:service_type>/',
         ServicesDetails.as_view(), name='service_detail'),
]
