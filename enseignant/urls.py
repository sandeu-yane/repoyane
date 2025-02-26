"""
URL configuration for mon_projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   
    path('', views.tab_enseignant, name="tab_enseignant"),
  path('gestion_assiduite/', views.gestion_assiduite, name="gestion_assiduite"),
  path('gestion-presences/', views.gestion_presences, name='gestion_presences'),
  path('enregistrer_assiduite/', views.enregistrer_assiduite, name='enregistrer_assiduite'),
  #path('get-matieres/<int:niveau_id>/', views.get_matieres_par_niveau, name='get_matieres_par_niveau'), # url de la fonction de trier des matiere par nivveau
  path('get-eleves/', views.get_eleves, name='get_eleves'),
  path('gestion_notes/', views.gestion_notes, name='gestion_notes'),
  path('add_assiduite/', views.add_assiduite, name='add_assiduite'),
]
