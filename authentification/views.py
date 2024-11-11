from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from .models import Utilisateur

# Create your views here.
# la vue de la page authentification
def connexion(request):

     #vérifions si une session du site est ouverte et affichons la page en fonction de ses privilèges sur le site
    if request.session.has_key('email'):

       if request.session["privilege"] == "P":

            return redirect("accueil_parent")

       elif request.session["privilege"] == "AD":

           return redirect("tab_administrateur")
       
       elif request.session["privilege"] == "E":

           return redirect("tab_enseignant")
    return render (request, template_name="login/login.html")

def login_request(request):
    # Récupérons les données de notre formulaire de connexion

    email = request.POST.get('email')
    password = request.POST.get('password')

    if request.method == 'POST':
        # Vérification de l'authenticité de l'utilisateur
        user = authenticate(username=email, password=password)

        # Récupérons le privilège de l'utilisateur
        utilisateur = get_object_or_404(Utilisateur, email=email)

        # Affichons les dashboards correspondant aux utilisateurs
        if user is not None:
            # Initialisons les sessions de l'utilisateur
            login(request, user)
            request.session["username"] = utilisateur.username
            request.session["prenom"] = utilisateur.prenom
            request.session["email"] = utilisateur.email
            request.session["privilege"] = utilisateur.privilege

            # Affichons les pages d'accueil des utilisateurs en fonction de leurs privilèges
            if utilisateur.privilege == "P" and utilisateur.etatCompte == "A":
                return redirect("accueil_parent")  # Redirection vers la page d'accueil du parent
            elif utilisateur.privilege == "AD" and utilisateur.etatCompte == "A":
                return redirect("tab_administrateur")  # Redirection vers la page d'accueil de l'administrateur
            elif utilisateur.privilege == "E" and utilisateur.etatCompte == "A":
                return redirect("tab_enseignant")  # Redirection vers la page d'accueil de l'enseignant

        else:
            # Si l'utilisateur est None, renvoyons un message d'erreur
            return HttpResponse("Email ou mot de passe incorrect", status=401)

    # Si la méthode de requête n'est pas POST, retournons à la page de connexion
    return redirect("connexion")


#login_required
#def deconnexion(request):
    #del request.session["connexion"]
    #logout(request)

    #return redirect(reverse("connexion"))

@login_required
def deconnexion(request):
    del request.session["username"]
    logout(request)

    return redirect(reverse("connexion"))



