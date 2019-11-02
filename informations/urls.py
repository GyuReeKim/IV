from django.urls import path
from . import views

app_name = "informations"

urlpatterns = [
    path('', views.index, name="index"),

    # character_list
    path('survivor/', views.survivor_list, name="survivor_list"),
    path('hunter/', views.hunter_list, name="hunter_list"),

    # character_detail
    path('survivor/<int:survivor_id>/', views.survivor_detail, name="survivor_detail"),
    path('hunter/<int:hunter_id>/', views.hunter_detail, name="hunter_detail"),

    # character_like
    path('survivor/<int:survivor_id>/like/', views.survivor_like, name="survivor_like"),
    path('hunter/<int:hunter_id>/like/', views.hunter_like, name="hunter_like"),
]
