from django.db import models
from authentification.models import Utilisateur
# Create your models here.




class Parent(Utilisateur):
    profession = models.CharField(max_length=100)
    nombres_enfants = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.prenom} {self.username} "
