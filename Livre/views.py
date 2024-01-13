from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from Livre.models import Document
from Bibliotheque import settings
import os
import mimetypes

def index(request):
    return render(request, 'livre/index.html')

def liste(request):
    documents = Document.objects.all()  # Mise à jour ici
    return render(request, 'livre/liste.html', context={"documents": documents})  # Mise à jour ici

def document_detail(request, id):  # Mise à jour ici
    document = get_object_or_404(Document, id=id)  # Mise à jour ici
    return render(request, 'livre/detail.html', context={"document": document})  # Mise à jour ici

def telechargement_document(request, id):  # Mise à jour ici
    document = get_object_or_404(Document, id=id)  # Mise à jour ici
    chemin_fichier = document.Fichier.path  # Mise à jour ici

    if os.path.exists(chemin_fichier):
        try:
            with open(chemin_fichier, 'rb') as fichier:
                content_type, encoding = mimetypes.guess_type(chemin_fichier)
                contenu_fichier = fichier.read()
                response = HttpResponse(contenu_fichier, content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{document.Titre}"'  # Mise à jour ici
                print(f'Chemin du fichier : {chemin_fichier}')
                print(f'Taille du fichier avant la réponse : {os.path.getsize(chemin_fichier)} bytes')
                return response
        except FileNotFoundError:
            message = 'Le fichier demandé n\'a pas été trouvé.'
        except PermissionError:
            message = 'Permission refusée pour accéder au fichier.'
        except Exception as e:
            print(f"Erreur lors de l'ouverture du fichier : {e}")
            message = 'Une erreur est survenue lors du téléchargement du document.'  # Mise à jour ici
    else:
        return render(request, 'livre/erreur.html', {'message': 'Le document demandé n\'existe pas.'})  # Mise à jour ici

def recherche_document(request):  # Mise à jour ici
    query = request.GET.get('search')
    documents = Document.objects.filter(Titre__icontains=query) if query else Document.objects.all()  # Mise à jour ici

    context = {
        'documents': documents,  # Mise à jour ici
        'query': query,
        'aucun_resultat': not documents.exists() if query else False,  # Mise à jour ici
    }

    return render(request, 'livre/recherche_livre.html', context)
