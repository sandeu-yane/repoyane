import json
from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from administrateur.models import Eleve, EmploiDeTemp, Matiere, Niveau, Salle
from enseignant.models import Assiduite, Note
from parent.models import Parent
# la vue du dashboad du parent
"""@login_required
def accueil_parent(request):
     if request.session["privilege"] != "P":

        return HttpResponse("vous n'avez pas  accès à cette page !")

     return render(request,template_name= "tableau/base.html")

@csrf_exempt
def get_students_by_phone(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone = data.get('phone')

        # Rechercher les élèves par numéro de téléphone
        students = Eleve.objects.filter(telephone=phone).values('id', 'nom', 'prenom', 'sexe', 'salle')
        
        return JsonResponse({'students': list(students)})
    return JsonResponse({'error': 'Invalid request method'}, status=400)"""


@login_required
def accueil_parent(request):
    if request.user.privilege != "P":  # Vérifie si c'est bien un parent
        return HttpResponse("Vous n'avez pas accès à cette page!")

    # Récupérer l'utilisateur connecté et vérifier si c'est un parent
    try:
         parent = Parent.objects.filter(email=request.user.email).first()
    except Parent.DoesNotExist:
        return HttpResponse("Aucun parent trouvé.")

    # Récupérer les élèves qui ont le même numéro de téléphone que le parent
    enfants = Eleve.objects.filter(tel_parent=parent.numero_tel).values(
        'id', 'noms', 'prenoms', 'sexe', 'salle'
    )

    # Vérifier s'il y a des enfants
    message = "Aucun enfant trouvé." if not enfants else None

    return render(request, "tableau/base.html", {'enfants': list(enfants), 'message': message})

# code pour consulter l'assiduité 
def consulter_assiduite(request):
    print("/////////////")
    if request.method == 'POST':
        eleve_id = request.POST.get('eleve_id')
        date = request.POST.get('date')

        if not eleve_id or not date:
            return JsonResponse({'success': False, 'message': 'Élève ou date manquante.'})

        # Récupérer les assiduités de l'élève pour la date donnée
        assiduites = Assiduite.objects.filter(eleve_id=eleve_id, date=date).values(
            'matiere__nom', 'present', 'observation', 'date', 'heure'
        )

        data = list(assiduites)  # Convertir en liste de dictionnaires
        return JsonResponse({'success': True, 'assiduites': data})

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'})



def consulter_notes(request):
    if request.method == 'POST':
        eleve_id = request.POST.get('eleve_id')
        sequence = request.POST.get('sequence')

        if not eleve_id or not sequence:
            return JsonResponse({'success': False, 'message': 'Élève ou séquence manquante.'})

        # Récupérer les notes de l'élève pour la séquence donnée
        notes = Note.objects.filter(eleve_id=eleve_id, sequence=sequence).values(
            'matiere__nom', 'note', 'appreciation', 'sequence'
        )

        data = list(notes)  # Convertir en liste de dictionnaires
        return JsonResponse({'success': True, 'notes': data})

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'})

# code pour consulter l'emploie
from django.http import JsonResponse


def consulter_emploi_temps(request):
    if request.method == 'POST':
        salle_id = request.POST.get('salle_id')

        if not salle_id:
            return JsonResponse({'success': False, 'message': 'Salle manquante.'})

        # Récupérer l'emploi du temps de la salle
        emploi_du_temps = EmploiDeTemp.objects.filter(salle_id=salle_id).values(
            'jour', 'heure_debut', 'heure_fin', 'matiere'
        )

        # Construire le tableau en dictionnaire
        emploi_dict = []
        jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

        for emploi in emploi_du_temps:
            emploi_data = {
                "heure_debut": emploi["heure_debut"].strftime("%H:%M"),
                "heure_fin": emploi["heure_fin"].strftime("%H:%M"),
            }
            for jour in jours:
                emploi_data[jour] = emploi["matiere"] if emploi["jour"] == jour else ""

            emploi_dict.append(emploi_data)

        return JsonResponse({'success': True, 'emploi_du_temps': emploi_dict})

    return JsonResponse({'success': False, 'message': 'Méthode non autorisée.'})
 