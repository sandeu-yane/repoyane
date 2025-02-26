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

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.tab_administrateur, name="tab_administrateur"),
    path('addenseignant/', views.addenseignant, name="addenseignant"),
    path('addparent/', views.addparent, name="addparent"),
    path('addsalle/', views.addsalle, name="addsalle"),
    path('addmatiere/', views.addmatiere, name="addmatiere"),
    #path('get_enseignant/<int:id>/', views.get_enseignant, name="get_enseignant"),
    #path(' delete_enseignant/<int:id>/', views.delete_enseignant, name='delete_enseignant'),
    path('addeleve/', views.addeleve, name="addeleve"),
    path('get_enseignant/<int:id>/', views.get_enseignant, name='get_enseignant'),
    path('modifier_enseignant/<int:id>/', views.modifier_enseignant, name='modifier_enseignant'),
]

