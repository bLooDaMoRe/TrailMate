from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trails.urls')),
    path('favorites/', include('favorites.urls')),
    path('catalog/', include('catalog.urls')),
]

handler404 = 'django.views.defaults.page_not_found'