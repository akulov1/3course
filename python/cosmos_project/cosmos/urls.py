from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('planet/<int:planet_id>/', views.planet_detail, name='planet_detail'),
    path('add/', views.add_planet, name='add_planet'),
    path('planet/<int:planet_id>/edit/', views.edit_planet, name='edit_planet'),

]
