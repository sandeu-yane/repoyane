from django.db import models
from authentification.models import Utilisateur

# Classe Enseignant
class Enseignant(Utilisateur):
    matiere_enseignee = models.CharField(max_length=100)
    classe = models.CharField(max_length=200)
    niveau = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.prenom} {self.username}"

# Classe Assiduite
class Assiduite(models.Model):
    eleve = models.ForeignKey('administrateur.Eleve', on_delete=models.CASCADE)
    matiere = models.ForeignKey('administrateur.Matiere', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=False)
    observation = models.TextField(blank=True, null=True)
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.date} - {self.enseignant}"

# Classe Note
class Note(models.Model):
    eleve = models.ForeignKey('administrateur.Eleve', on_delete=models.CASCADE)
    matiere = models.ForeignKey('administrateur.Matiere', on_delete=models.CASCADE)
    note = models.FloatField()
    observation = models.TextField(blank=True, null=True)
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.CASCADE)
   

    def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.note}"
