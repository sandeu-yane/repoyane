from urllib import request
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required


# la vue du dashbord de l'enseignant
@login_required
def tab_enseignant(request):

     if request.session["privilege"] != "E":

         return HttpResponse("vous n'avez pas accès à cette page !")
     return render (request, template_name="tableau/indexenseignant.html")