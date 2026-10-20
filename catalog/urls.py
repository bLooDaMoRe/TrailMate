from django.urls import path
from . import views

urlpatterns = [
    path('features/', views.feature_list, name='feature-list'),
    path('features/add/', views.feature_create, name='feature-create'),
]