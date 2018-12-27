from django.urls import path
from . import views


app_name = "lecture"


urlpatterns = [
    path('', views.index, name="index"),
    path('dark_matter/', views.dark_matter, name="dark_matter"),
    path('quantum_mechanics/', views.quantum_mechanics, name="quantum_mechanics"),
    path('planet_death/', views.planet_death, name="planet_death"),
]