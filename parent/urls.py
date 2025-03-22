
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.accueil_parent, name="accueil_parent"),
    #path('api/assiduite/<int:eleve_id>/<str:date>/', views.get_assiduite, name="get_assiduite"),
    path('consulter_assiduite/', views.consulter_assiduite, name="consulter_assiduite"),
    path('consulter_notes/', views.consulter_notes, name="consulter_notes"),
    path('consulter_emploi_temps/', views.consulter_emploi_temps, name="consulter_emploi_temps"),
]
