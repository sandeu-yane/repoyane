import json
from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
import enseignant
from django.shortcuts import render, redirect
from django.utils import timezone
from administrateur.models import Eleve, Matiere, Niveau, Salle # Importer Eleve depuis administrateur.models
from .models import Assiduite,  Enseignant
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



# la vue du dashbord de l'enseignant
@login_required
def tab_enseignant(request):

     if request.session["privilege"] != "E":
         
        

        return HttpResponse("vous n'avez pas accès à cette page !")
     niveaux = Niveau.objects.all()
     matieres = Matiere.objects.all()
     salles = Salle.objects.all()
    
     return render (request, "tableau/indexenseignant.html", {"salles":salles,"matieres":matieres,
        'enseignants': enseignant,
         'niveaux': niveaux,
        'date': timezone.now().date(),
        'heure': timezone.now().time(),})
       



@login_required
def gestion_assiduite(request):
    eleves = Eleve.objects.all()
    matieres = Matiere.objects.all()
    enseignants = Enseignant.objects.all()
    enseignant_id = request.user.id  # Récupère l'ID de l'enseignant connecté

    return render(request, 'indexenseignant.html', {
        'eleves': eleves,
        'matieres': matieres,
        'enseignants': enseignants,
        'date': timezone.now().date(),
        'heure': timezone.now().time(),
        'enseignant_id': enseignant_id  # Passer l'ID de l'enseignant au template
    })
           
"""def enregistrer_assiduite(request):
    if request.method == 'POST':
        niveau_id = request.POST.get("niveau")
        matiere_id = request.POST.get("matiere")
        salle_id = request.POST.get("salle")

        try:
            niveau = Niveau.objects.get(id=niveau_id)
            salle = Salle.objects.get(id=salle_id)
            matiere = Matiere.objects.get(id=matiere_id)
        except (Salle.DoesNotExist, Matiere.DoesNotExist):
            return JsonResponse({'error': 'Salle ou matière non trouvée.'}, status=404)

        eleves = Eleve.objects.filter(salle=salle)
        eleves_data = [
            {
                'id': eleve.id,
                'nom': eleve.noms,
                'prenom': eleve.prenoms,
                'sexe': eleve.sexe,
                'classe': eleve.salle.nom,
            }
            for eleve in eleves
        ]

        return JsonResponse({'eleves': eleves_data})

    return JsonResponse({'error': 'Requête non autorisée'}, status=400) """
#code pour afficher les matieres et classe dans le formulaire
def gestion_presences(request):
    niveaux = Niveau.objects.all()
    matieres = Matiere.objects.all()
    salles = Salle.objects.all()
    print ("Salles")
    return render(request, 'indexenseignant.html', {'niveaux': niveaux, 'matieres': matieres, 'salles': salles})

# nouveau code essaie

def get_eleves(request):
    if request.method == 'POST':
        matiere_id = request.POST.get('matiere')
        salle_id = request.POST.get('salle')
        eleves = Eleve.objects.filter(classe__salle__id=salle_id, classe__matiere__id=matiere_id)
        eleves_data = [
            {
                'nom': eleve.nom,
                'prenom': eleve.prenom,
                'sexe': eleve.sexe,
                'classe': eleve.classe.nom,
                'date': '',  # Ajouter la logique pour la date
                'heure': '',  # Ajouter la logique pour l'heure
            } for eleve in eleves
        ]
        return JsonResponse({'eleves': eleves_data})
    return JsonResponse({'error': 'Invalid request'}, status=400)

# code pour la gestion des notes dans le formulaire
def gestion_notes(request):
    if request.method == 'POST':
        matiere_id = request.POST.get("matiere")
        salle_id = request.POST.get("salle")

        try:
            salle = Salle.objects.get(id=salle_id)
            matiere = Matiere.objects.get(id=matiere_id)
        except (Salle.DoesNotExist, Matiere.DoesNotExist):
            return JsonResponse({'error': 'Salle ou matière non trouvée.'}, status=404)

        eleves = Eleve.objects.filter(salle=salle)
        eleves_data = [
            {
                'id': eleve.id,
                'nom': eleve.noms,
                'prenom': eleve.prenoms,
                'sexe': eleve.sexe,
                'classe': eleve.salle.nom,
            }
            for eleve in eleves
        ]

        return JsonResponse({'eleves': eleves_data})

    return JsonResponse({'error': 'Requête non autorisée'}, status=400)

# code pour trier les matieres par niveau 

"""def get_matieres_par_niveau(request, niveau_id):
    //Renvoie les matières associées à un niveau donné
    matieres = Matiere.objects.filter(niveau_id=niveau_id).values('id', 'nom')
    print("/////////////////////////////////////////////////////////////////////")
    return JsonResponse({'matieres': list(matieres)}) """


#code exact pour l'assiduité
@csrf_exempt
def enregistrer_assiduite(request):
    if request.method == 'POST':
        niveau_id = request.POST.get("niveau")  # Récupère l'ID du niveau
        salle_id = request.POST.get("salle")    # Récupère l'ID de la salle/classe
        print(f"🔹 Niveau reçu: {niveau_id}")
        print(f"🏫 Salle reçue: {salle_id}")

        # Vérifier si le niveau existe
        try:
            niveau = Niveau.objects.get(id=niveau_id)
            print(f"✅ Niveau trouvé : {niveau}")

            # Récupérer les matières associées au niveau
            matieres = Matiere.objects.filter(niveau=niveau).values('id', 'nom')
            #print(f"📚 Matières trouvées : {list(matieres)}")

            # Récupérer les élèves de la salle
            if salle_id:
                try:
                    salle = Salle.objects.get(id=salle_id)
                    eleves = Eleve.objects.filter(salle=salle)
                    eleves_data = [
                        {
                            'id': eleve.id,
                            'nom': eleve.noms,
                            'prenom': eleve.prenoms,
                            'sexe': eleve.sexe,
                            'classe': eleve.salle.nom,
                        }
                        for eleve in eleves
                    ]
                    print(f"👨‍🎓 Élèves trouvés : {eleves_data}")

                    return JsonResponse({'matieres': list(matieres), 'eleves': eleves_data})

                except Salle.DoesNotExist:
                    print("❌ Salle introuvable !")
                    return JsonResponse({'error': 'Salle introuvable.'}, status=404)

            return JsonResponse({'matieres': list(matieres), 'eleves': []})

        except Niveau.DoesNotExist:
            print("❌ Niveau introuvable !")
            return JsonResponse({'error': 'Niveau introuvable.'}, status=404)

    return JsonResponse({'error': 'Requête non autorisée'}, status=400) 




# code pour enreistrer l'assiduité dans la base de donnée 


from .models import Assiduite
from .serializers import AssiduiteSerializer

@api_view(['POST'])
def add_assiduite(request):
    print("🔹 Requête reçue :", request.data)  # Debugging

    eleves_data = request.data.get("eleves", [])
    matiere_id = request.data.get("matiere")
    salle_id = request.data.get("salle")
    enseignant_id = request.data.get("enseignant")

    assiduites = []
    for eleve in eleves_data:
        assiduites.append(Assiduite(
            eleve_id=eleve['id'],
            matiere_id=matiere_id,
            salle_id=salle_id,
            enseignant_id=enseignant_id,
            present=eleve['present'],
            observation=eleve.get('observation', '')
        ))

    Assiduite.objects.bulk_create(assiduites)  # 🌟 Insertion rapide !

    return Response({"success": True, "message": "Assiduité enregistrée avec succès"})



