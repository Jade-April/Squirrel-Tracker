from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sightings/',views.list_sightings),
    path('map/',views.get_map),
    path('sightings/stats',views.general_state),
]
