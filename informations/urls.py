from django.urls import path
from . import views

app_name = "informations"

urlpatterns = [
    path('', views.index, name="index"),
    
    # character_list
    path('survivor/', views.survivor_list, name="survivor_list"),
    path('hunter/', views.hunter_list, name="hunter_list"),
]
