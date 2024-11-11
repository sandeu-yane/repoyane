from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from enseignant.models import Enseignant
from administrateur.models import Salle
from administrateur.models import Eleve
from parent.models import Parent

# la vus du dashbord de l'administrateur
@login_required
def tab_administrateur(request):

     if request.session["privilege"] != "AD":

         return HttpResponse("vous n'avez pas accès à cette page !")
     enseignant = Enseignant.objects.filter(privilege="E", affiche="A")
     parent = Parent.objects.all()
     eleve =Eleve.objects.all()
     salle =Salle.objects.all()
       # Combinez les deux dictionnaires dans un seul
     context = {
        "liste_enseignant": enseignant,
        "liste_parent": parent,
        "liste_salle": salle,
        "liste_eleve": eleve,
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
        return HttpResponse("Gars, tu n'as accès à cette page !")

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
        return HttpResponse("Gars, tu n'as accès à cette page !")

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
        classe = request.POST.get('classe')
        tel_parent = request.POST.get('tel_parent')

        # Vérifier que tous les champs requis sont présents
        if not (noms and prenoms and sexe and quartier and date_naissance and classe and tel_parent):
            return JsonResponse({'success': False, 'error': 'Tous les champs sont obligatoires.'}, status=400)

        # Créer un nouvel élève
        new_eleve = Eleve(
            noms=noms,
            prenoms=prenoms,
            sexe=sexe,
            quartier=quartier,
            date_naissance=date_naissance,
            classe=classe,
            tel_parent=tel_parent
        )
        new_eleve.save()

    # Dans tous les cas, récupérer la liste des élèves pour l'afficher
    eleve = Eleve.objects.all()

    # Retourner la page avec la liste des élèves, qu'il s'agisse d'une requête GET ou après une requête POST réussie
    return render(request, "tableau/indexadmin.html", {'liste_eleve': eleve})

# la fonction qui permet d'afficher le contenu du formulaire lors d'une modification 
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





