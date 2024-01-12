from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from Livre.models import Livre
from Bibliotheque import settings
import os
import mimetypes

# eto no icreena ny vue, zany oe hahafahana mampiseho ny page HTML any @ navigateur, sady mi'definir ny fonction sy ny logique rehetra mahakasika an'ilay page

def index(request):
    return render(request, 'livre/index.html')

#fonction hampisehoana ny livre any @ page html
def liste(request):
    livres = Livre.objects.all()
    return render(request, 'livre/liste.html', context={"livres": livres})

#fonction detail livre
def livre_detail(request, id):
    livre = get_object_or_404(Livre, id=id)
    return render(request, 'livre/detail.html', context={"livre":livre})

#fonction telechargement livre
def telechargement_livre(request, id):
    livre = get_object_or_404(Livre, id=id)
    chemin_fichier = livre.Fichier.path
     
     # Si le fichier existe, retournez le en réponse
    if os.path.exists(chemin_fichier):
        try:
            with open(chemin_fichier, 'rb') as fichier:
                content_type, encoding = mimetypes.guess_type(chemin_fichier)
                contenu_fichier = fichier.read()
                response = HttpResponse(contenu_fichier, content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{livre.Titre}"'
                print(f'Chemin du fichier : {chemin_fichier}')
                print(f'Taille du fichier avant la réponse : {os.path.getsize(chemin_fichier)} bytes')
                return response
        except FileNotFoundError:
            message = 'Le fichier demandé n\'a pas été trouvé.'
        
        except PermissionError:
            message = 'Permission refusée pour accéder au fichier.'
        except Exception as e:
            print(f"Erreur lors de l'ouverture du fichier : {e}")
            message = 'Une erreur est survenue lors du téléchargement du livre.'
        
    else:
        # Gérez le cas où le fichier n'existe pas
        return render(request, 'livre/erreur.html', {'message': 'Le livre demandé n\'existe pas.'})
    
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


