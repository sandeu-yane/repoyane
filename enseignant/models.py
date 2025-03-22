
from django.db import models
from authentification.models import Utilisateur
from django.utils import timezone
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
    salle = models.ForeignKey('administrateur.Salle', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # Date de création
    heure = models.DateTimeField(default=timezone.now)  # Ajout de l'heure 
    present = models.BooleanField(default=False)
    observation = models.TextField(blank=True, null=True)
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.date} - {self.enseignant}"

# Classe Note
class Note(models.Model):
    eleve = models.ForeignKey('administrateur.Eleve', on_delete=models.CASCADE)
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.CASCADE)
    matiere = models.ForeignKey('administrateur.Matiere', on_delete=models.CASCADE)
    salle = models.ForeignKey('administrateur.Salle', on_delete=models.CASCADE)
    note = models.FloatField()
    appreciation = models.TextField(blank=True, null=True)
    sequence = models.CharField(max_length=50, choices=[
        ('1', 'Séquence 1'), ('2', 'Séquence 2'),
        ('3', 'Séquence 3'), ('4', 'Séquence 4'),
        ('5', 'Séquence 5'), ('6', 'Séquence 6')
    ])
    enseignant = models.ForeignKey('enseignant.Enseignant', on_delete=models.CASCADE)
   
def __str__(self):
        return f"{self.eleve} - {self.matiere} - {self.note} - {self.sequence}"
