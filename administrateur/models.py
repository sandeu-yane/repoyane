
from django.db import models
from enseignant.models import Enseignant


# declaration de la classe salle
class Salle(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=255)
    effectifs = models.IntegerField(null=True, blank=True)  # Peut être nul et non obligatoire
    Id_enseignant = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='salles')
    Id_eleve = models.ForeignKey('Eleve', on_delete=models.SET_NULL, null=True, related_name='salles')

    def __str__(self):
        return self.nom

# declaration de la classe eleve
class Eleve(models.Model):
    noms = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)  # Par exemple: 'M' pour masculin, 'F' pour féminin
    date_naissance = models.DateField()
    quartier = models.CharField(max_length=255)
    classe = models.CharField(max_length=50)
    tel_parent = models.CharField(max_length=20, blank=True, null=True)  # Peut être nul ou vide

    def __str__(self):
        return f"{self.noms} {self.prenoms}"
    




    