

#ato ndray no mametraka ny chemin, ohatra oe: '/admin/'

from django.contrib import admin
from django.urls import path
from Livre.views import index, liste, document_detail, telechargement_document, recherche_document
from django.conf.urls.static import static
from Bibliotheque import settings


urlpatterns = [
    path('', index, name='index'),
    path('liste/', liste, name='liste'),
    path('document/<int:id>', document_detail, name='document_detail'),
    path('telechargement-document/<int:id>', telechargement_document, name='telechargement_document'),  # Changement ici
    path('recherche/', recherche_document, name='recherche_document'),  # Changement ici
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

