
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):

    ETAT_COMPTE_CHOICES = [
        ('A', 'Active'),
        ('D', 'Desactive'),

    ]

    PRIVILEGE_UTILISATEUR_CHOICES = [
        ('P', 'Parent'),
        ('AD', 'Administrateur'),
        ('E', 'enseignant'),

    ]

    AFFICHE_UTILISATEUR_CHOICES = [
        ('A', 'Affiche'),
        ('C', 'Cache'),

    ]


    username = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    #sexe = models.CharField(max_length=100)
    numero_tel = models.IntegerField()
    email = models.EmailField(unique=True)
    etatCompte = models.CharField(max_length=100, choices=ETAT_COMPTE_CHOICES)
    DateCreation = models.DateTimeField(default=datetime.now())
    privilege = models.CharField(max_length=100, choices=PRIVILEGE_UTILISATEUR_CHOICES)
    affiche = models.CharField(max_length=100, choices=AFFICHE_UTILISATEUR_CHOICES)
    derniere_modification = models.CharField(max_length=100, null=True)
    heure_derniere_modification = models.DateTimeField(null=True)

  

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "prenom",  "password", "etatCompte", "privilege", "numero_tel"]




    def __str__(self):
        return self.email


