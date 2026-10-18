from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trails/', views.trail_list, name='trail-list'),
    path('locations/', views.location_list, name='location-list'),
    path('locations/add/', views.location_create, name='location-create'),
    path('trails/add/', views.trail_create, name='trail-create'),
    path('trails/<int:pk>/edit/', views.trail_edit, name='trail-edit'),
    path('trails/<int:pk>/delete/', views.trail_delete, name='trail-delete'),
    path('locations/<int:pk>/edit/', views.location_edit, name='location-edit'),
    path('locations/<int:pk>/delete/', views.location_delete, name='location-delete'),
    path('trails/<int:pk>/', views.trail_detail, name='trail-detail'),
]
