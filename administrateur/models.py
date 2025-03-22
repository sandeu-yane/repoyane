from django.db import models

from parent.models import Parent

# Classe Salle
class Salle(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=255)
    effectifs = models.IntegerField(null=True, blank=True)
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.SET_NULL, null=True, related_name='salles')
    niveau = models.ForeignKey('administrateur.Niveau', on_delete=models.CASCADE)


    def __str__(self):
        return self.nom

# Classe Eleve
class Eleve(models.Model):
    #parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='enfants') 
    noms = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    sexe = models.CharField(max_length=10)
    date_naissance = models.DateField()
    quartier = models.CharField(max_length=255)
    classe = models.CharField(max_length=50)
    tel_parent = models.CharField(max_length=20, blank=True, null=False)
    salle = models.ForeignKey('administrateur.Salle', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.noms} {self.prenoms}"

# Classe Matiere
class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    coefficient = models.IntegerField()
    niveau = models.ForeignKey('administrateur.Niveau', on_delete=models.CASCADE)
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.CASCADE)


    def __str__(self):
        return self.nom

 #Classe NIVEAU
class Niveau(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
      return self.nom

#classe emploie 
class EmploiDeTemp(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20)  # Exemple: Lundi, Mardi, etc.
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    matiere = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.salle} - {self.jour} {self.heure_debut} - {self.heure_fin}"