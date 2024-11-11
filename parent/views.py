from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

# la vue du dashboad du parent
@login_required
def accueil_parent(request):
     if request.session["privilege"] != "P":

        return HttpResponse("vous n'avez pas  accès à cette page !")

     return render(request,template_name= "tableau/base.html")
