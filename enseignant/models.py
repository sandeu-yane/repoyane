from django.db import models

from datetime import datetime

from authentification.models import Utilisateur

class Enseignant(Utilisateur):
    matiere = models.CharField(max_length=100)
    classe = models.CharField(max_length=200)
    niveau = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.prenom} {self.username} "

