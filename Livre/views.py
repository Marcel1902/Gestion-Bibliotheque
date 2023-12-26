from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from Livre.models import Livre
from Bibliotheque import settings
import os

# eto no icreena ny vue, zany oe hahafahana mampiseho ny page HTML any @ navigateur, sady mi'definir ny fonction sy ny logique rehetra mahakasika an'ilay page

def index(request):
    return render(request, 'livre/index.html')

#fonction hampisehoana ny livre any @ page html
def liste(request):
    livres = Livre.objects.all()
    return render(request, 'livre/liste.html', context={"livres": livres})

#fonction detail livre
def livre_detail(request, slug):
    livre = get_object_or_404(Livre, slug=slug)
    return render(request, 'livre/detail.html', context={"livre":livre})

#fonction telechargement livre
def telechargement_livre(request, slug):
    livre = get_object_or_404(Livre, slug=slug)
    chemin_fichier = livre.Fichier.path
     
     # Si le fichier existe, retournez le en réponse
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'rb') as fichier:
            response = FileResponse(fichier, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="livre.Titre.pdf"'
            return response
    
    else:
        # Gérez le cas où le fichier n'existe pas
        return render(request, 'erreur.html', {'message': 'Le livre demandé n\'existe pas.'})
    
# fonction recherche livre
def recherche_livre(request):
    query = request.GET.get('search')
    livres = Livre.objects.filter(Titre__icontains=query) if query else Livre.objects.all()
    
    context = {
        'livres': livres,
        'query': query,
        'aucun_resultat': not livres.exists() if query else False,
    }

    return render(request, 'livre/recherche_livre.html', context)


