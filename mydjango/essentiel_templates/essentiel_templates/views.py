from django.shortcuts import render
import datetime
from .Utilitaires import Etudiant

def index(request):
    return render(request, "index.html")

def view_static(request):
    return render(request, "temp_static.html")

def view_variables(request):
    vint = 10
    vfloat = 10.5
    vboolean = True
    vstring = "Bonjour"
    vdate = datetime.datetime.today()
    dictionnaire = {
        "vint" : vint,
        "vfloat" : vfloat,
        "vbool" : vboolean,
        "vstring" : vstring,
        "vdate" : vdate
    }
    return render(request, "temp_variables.html", context = dictionnaire)

def view_attributs(request):
    etudiant = Etudiant("Etud001", "Bahroun", "Najib", "M", 12.5)
    context = {"etud" : etudiant}
    return render(request, "temp_attributs_objet.html", context)

def view_alternatives(request):
    etudiant = Etudiant("Etud002", "Chamsoun", "Meryme", "F", 19.5)
    context = {"etud" : etudiant}
    return render(request, "temp_alternatives.html", context)

def view_boucle(request):
    classe = []
    classe.append(Etudiant("Etud001", "Bardoune", "Najib", "M", 12.5))
    classe.append(Etudiant("Etud002", "Naimoune", "Ali", "M", 8.5))
    classe.append(Etudiant("Etud003", "Misbahoune", "Nadia", "F", 15.5))
    classe.append(Etudiant("Etud004", "Chamsoune", "Meryem", "F", 19.5))
    classe.append(Etudiant("Etud005", "Mardiyoune", "Fouad", "F", 13.5))
    classe.append(Etudiant("Etud006", "Mouttakioune", "Said", "F", 10.5))
    
    # Calcul de la moyenne de la classe
    S = 0
    for etudiant in classe:
        S += etudiant.note
    moyenne = round(S/len(classe), 2)
    
    classe_vide = []
    context = {"classe": classe, "moyenne": moyenne, "classe_vide": classe_vide}
    return render(request, "temp_boucle.html", context)