import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view

from enseignant.models import Enseignant
from administrateur.models import EmploiDeTemp, Matiere, Niveau, Salle
from administrateur.models import Eleve
from parent.models import Parent
from rest_framework.response import Response
from django.http import JsonResponse
# la vus du dashbord de l'administrateur
@login_required
def tab_administrateur(request):

     if request.session["privilege"] != "AD":

         return HttpResponse("vous n'avez pas accès à cette page !")
     enseignant = Enseignant.objects.filter(privilege="E", affiche="A")
     parent = Parent.objects.all()
     eleve =Eleve.objects.all()
     salle =Salle.objects.all()
     niveaux = Niveau.objects.all()
     matieres = Matiere.objects.all()
     salle = Salle.objects.all()
     emploi = EmploiDeTemp.objects.all()
       # Combinez les deux dictionnaires dans un seul
     context = {
        "liste_enseignant": enseignant,
        "liste_parent": parent,
        "liste_salle": salle,
        "liste_eleve": eleve,
        "salles":salle,
        "niveaux":niveaux,
        "emploi" :emploi,
    }

     return render(request, "tableau/indexadmin.html", context   )


#la fonction qui permet d'ajouter un enseignant
@login_required
def addenseignant(request):
    if request.session["privilege"] != "AD":
        return HttpResponse("Gars, tu n'as accès à cette page !")

    if request.method == "POST":
        # Récupérons les informations pour la création d'un utilisateur
        noms = request.POST['noms']
        prenom = request.POST['prenom']
        #sexe = request.POST['sexe']
        email = request.POST['email']
        matiere = request.POST['matiere']
        niveau = request.POST['niveau']
        password = "12345678"
        telephone = request.POST['telephone']

        # Créer un nouvel enseignant
        new_enseignant = Enseignant(username=noms, prenom=prenom,   email=email, matiere=matiere, niveau=niveau, numero_tel=telephone,  privilege="E", etatCompte="A", affiche="A")
        new_enseignant.set_password(password)
        new_enseignant.save()

        # Récupérer la liste actualisée des enseignants après l'ajout
        enseignants = Enseignant.objects.all()
        return render(request, "tableau/indexadmin.html", {
           
            'liste_enseignant': enseignants
        })
    #for e in enseignants:
        #print(e.id + " "+ e.username +" "+ e.prenom + " "+ e.numero_tel)

    
    # Affichage initial de la liste des enseignants
    enseignants = Enseignant.objects.all()
    return render(request, "tableau/indexadmin.html", {'liste_enseignant': enseignants})


#la fonction qui permet d'ajouter un parent
@login_required
def addparent(request):
    if request.session["privilege"] != "AD":
        return HttpResponse(" tu n'as accès à cette page !")

    if request.method == "POST":
        # Récupérons les informations pour la création d'un utilisateur
        noms = request.POST['noms']
        prenom = request.POST['prenom']
        #sexe = request.POST['sexe']
        email = request.POST['email']
        profession = request.POST['profession']
        nombres_enfants = request.POST['nombres_enfants']
        password = "12345678"
        telephone = request.POST['telephone']

        # Créer un nouvel parent
        new_parent = Parent(username=noms, prenom=prenom,   email=email, profession=profession, nombres_enfants=nombres_enfants, numero_tel=telephone,  privilege="P", etatCompte="A", affiche="A")
        new_parent.set_password(password)
        new_parent.save()

        # Récupérer la liste actualisée des parents après l'ajout
        parent = Parent.objects.all()
        return render(request, "tableau/indexadmin.html", {
           
            'liste_parent': parent
        })
    # Affichage initial de la liste des parents
    parent = Parent.objects.all()
    return render(request, "tableau/indexadmin.html", {'liste_parent': parent})



   
# vue pour ajouter une salle de classe
@login_required
def addsalle(request):
    if request.session.get("privilege") != "AD":
        return HttpResponse("tu n'as pas accès à cette page !")

    if request.method == "POST":
        # Récupérer les informations pour la création d'une salle
        nom = request.POST.get('nom')
        localisation = request.POST.get('localisation')
        effectifs = request.POST.get('effectifs')

        
            # Créer une nouvelle salle
        new_salle = Salle(nom=nom, localisation=localisation, effectifs=effectifs)
        new_salle.save()

            # Récupérer la liste actualisée des salles après l'ajout
        salles = Salle.objects.all()
        return render(request, "tableau/indexadmin.html", {'liste_salle': salles})
# code pour ajouter une matiere
@login_required
def addmatiere(request):
    if request.session.get("privilege") != "AD":
        return HttpResponse("tu n'as pas accès à cette page !")

    if request.method == "POST":
        # Récupérer les informations pour la création d'une salle
        nom = request.POST.get('nom')
        coefficient = request.POST.get('coefficient')
            # Créer une nouvelle salle
        new_matiere = Matiere(nom=nom,coefficient=coefficient )
        new_matiere.save()

            # Récupérer la liste actualisée des salles après l'ajout
        matieres = Matiere.objects.all()
        return render(request, "tableau/indexadmin.html", {'liste_matiere': matieres})
    
# la fonction qui permet d'ajouter un eleve
@login_required
def addeleve(request):
    if request.method == "POST":
        # Récupérons les informations pour la création d'un élève, avec une gestion des champs manquants
        noms = request.POST.get('noms')
        prenoms = request.POST.get('prenoms')
        sexe = request.POST.get('sexe')
        quartier = request.POST.get('quartier')
        date_naissance = request.POST.get('date_naissance')
        classe_id = request.POST.get('classe')  # Récupère l'ID de la salle (classe)
        tel_parent = request.POST.get('tel_parent')

        # Vérifier que tous les champs requis sont présents
        if not (noms and prenoms and sexe and quartier and date_naissance and classe_id and tel_parent):
            return JsonResponse({'success': False, 'error': 'Tous les champs sont obligatoires.'}, status=400)

        # Récupérer l'instance de la salle (classe)
        try:
            classe = Salle.objects.get(id=classe_id)  # Utilisation de l'ID pour obtenir l'instance
        except Salle.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Classe non trouvée.'}, status=400)

        # Créer un nouvel élève
        new_eleve = Eleve(
            noms=noms,
            prenoms=prenoms,
            sexe=sexe,
            quartier=quartier,
            date_naissance=date_naissance,
            salle=classe,  # Assigner l'instance de la salle
            tel_parent=tel_parent
        )
        new_eleve.save()
        
    # Récupérer la liste des élèves pour l'afficher
    eleve = Eleve.objects.all()

    # Retourner la page avec la liste des élèves, qu'il s'agisse d'une requête GET ou après une requête POST réussie
    return render(request, "tableau/indexadmin.html", {'liste_eleve': eleve, 'salles': Salle.objects.all()})

@login_required
def get_enseignant(request, id):
    if request.session.get("privilege") != "AD":
        return JsonResponse({'error': "Accès refusé."}, status=403)
    
    enseignant = get_object_or_404(Enseignant, id=id)
    
    # Retourner les informations de l'enseignant sous forme de JSON
    data = {
        'noms': enseignant.username,
        'prenom': enseignant.prenom,
        'sexe': enseignant.sexe,
        'telephone': enseignant.numero_tel,
        'email': enseignant.email,
        'matiere': enseignant.matiere,
        'niveau': enseignant.niveau
    }
    
    return JsonResponse(data)
# la fonction qui permet de modifier un enseignant 
@login_required
def modifier_enseignant(request, id):
    if request.session.get("privilege") != "AD":
        return JsonResponse({'error': "Accès refusé."}, status=403)
    enseignant = Enseignant.objects.get(id=id)
    enseignant = get_object_or_404(Enseignant, id=id)
    
    if request.method == "POST":
        enseignant.username = request.POST.get('noms')
        enseignant.prenom = request.POST.get('prenom')
        enseignant.sexe = request.POST.get('sexe')
        enseignant.numero_tel = request.POST.get('telephone')
        enseignant.email = request.POST.get('email')
        enseignant.matiere = request.POST.get('matiere')
        enseignant.niveau = request.POST.get('niveau')

        enseignant.save()
        
        return redirect('tab_administrateur')  # Rediriger après la modification
    
    #FONCTION POUR L'EMPLOIE DE TEMPS
@csrf_exempt
def filtrer_salles_par_niveau(request):
    if request.method == 'POST':
        niveau_id = request.POST.get("niveau")
        
        try:
            niveau = Niveau.objects.get(id=niveau_id)
            salles = Salle.objects.filter(niveau=niveau).values('id', 'nom')
            return JsonResponse({'salles': list(salles)})
        
        except Niveau.DoesNotExist:
            return JsonResponse({'error': 'Niveau introuvable.'}, status=404)

    return JsonResponse({'error': 'Requête non autorisée'}, status=400)

# code pour enregistrer l'emploie de temp
@csrf_exempt
def save_emploi_temps(request):
    if request.method == 'POST':
        salle_id = request.POST.get('salle')
        for key, value in request.POST.items():
            if key.startswith('matiere_'):
                # Extraire l'heure et le jour
                _, heure, jour = key.split('_')
                # Enregistrer chaque matière dans la base de données
                EmploiDeTemp.objects.create(salle_id=salle_id, heure=heure, jour=jour, matiere=value)

        return redirect('votre_vue_de_confirmation')
    
    
    from django.shortcuts import render
from .models import Salle, EmploiDeTemp

"""def emploi_temps_view(request):
    if request.method == 'POST':
        niveau_id = request.POST.get('niveau')
        salle_id = request.POST.get('salle')
        
        salle = get_object_or_404(Salle, id=salle_id)

        # Récupérer l'emploi du temps pour cette salle
        emploi_du_temps = EmploiDeTemp.objects.filter(salle=salle)

        # Construire une structure JSON avec les matières
        emploi_data = { jour: {heure: "" for heure in [
            "7h30 - 8h30", "8h30 - 9h30", "9h30 - 10h30",
            "10h30 - 11h30", "11h30 - 12h30", "12h30 - 13h30",
            "13h30 - 14h30", "14h30 - 15h30", "15h30 - 16h30"
        ]} for jour in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]}

        # Remplir avec les matières existantes
        for emploi in emploi_du_temps:
            emploi_data[emploi.jour][emploi.heure] = emploi.matiere.nom

        return JsonResponse({
            'salle': salle.nom,
            'emploi_du_temps': emploi_data
        })

    return render(request, 'tableau/indexadmin.html')"""

def emploi_temps_view(request):
    if request.method == 'POST':
        niveau_id = request.POST.get('niveau')
        salle_id = request.POST.get('salle')
        salle = Salle.objects.get(id=salle_id)

        # Récupérer l'emploi du temps pour la salle
        emploi_du_temps = EmploiDeTemp.objects.filter(salle=salle)

        # Construire les données sous forme de dictionnaire
        emploi_dict = {}
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
        heures = [
            "7h30 - 8h30", "8h30 - 9h30", "9h30 - 10h30",
            "10h30 - 11h30", "11h30 - 12h30", "12h30 - 13h30",
            "13h30 - 14h30", "14h30 - 15h30", "15h30 - 16h30"
        ]

        # Initialiser les cases vides
        for jour in jours:
            emploi_dict[jour] = {}
            for heure in heures:
                emploi_dict[jour][heure] = ""

        # Remplir avec les données existantes
        for emploi in emploi_du_temps:
            heure_range = emploi.heure_debut.strftime("%H:%M") + " - " + emploi.heure_fin.strftime("%H:%M")
            emploi_dict[emploi.jour][heure_range] = emploi.matiere  # ✅ Correction ici

        return JsonResponse({"emploi_du_temps": emploi_dict})

    return render(request, 'tableau/indexadmin.html')

# code pour save un emploie de temp 
from .serializers import EmploiDeTempSerializer
from datetime import datetime
import json
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(["POST"])
def add_emploi_temps(request):
    try:
        data = request.data  # ✅ DRF gère le parsing du JSON
        print("🔹 Requête reçue :", data)

        if "emploi_du_temps" not in data:
            return Response({"error": "Données invalides"}, status=400)

        emploi_objects = []
        for emploi in data["emploi_du_temps"]:
            salle_obj = get_object_or_404(Salle, id=int(emploi["salle"]))

            # ✅ Séparer l'heure en heure_debut et heure_fin
            heure_parts = emploi["heure"].split(" - ")
            if len(heure_parts) != 2:
                return Response({"error": "Format d'heure invalide"}, status=400)

            heure_debut = datetime.strptime(heure_parts[0], "%Hh%M").time()
            heure_fin = datetime.strptime(heure_parts[1], "%Hh%M").time()

            emploi_objects.append(
                EmploiDeTemp(
                    jour=emploi["jour"],
                    heure_debut=heure_debut,  # ⚠️ Correction du champ
                    heure_fin=heure_fin,      # ⚠️ Correction du champ
                    matiere=emploi["matiere"],
                    salle=salle_obj
                )
            )

        # 🌟 Insertion rapide en base de données
        EmploiDeTemp.objects.bulk_create(emploi_objects)

        return Response({"message": "Emploi du temps enregistré avec succès"}, status=201)

    except Exception as e:
        print("❌ ERREUR :", str(e))
        return Response({"error": "Erreur interne du serveur"}, status=500)
