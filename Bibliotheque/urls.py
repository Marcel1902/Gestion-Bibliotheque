

#ato ndray no mametraka ny chemin, ohatra oe: '/admin/'

from django.contrib import admin
from django.urls import path
from Livre.views import index, liste, livre_detail, telechargement_livre, recherche_livre
from django.conf.urls.static import static
from Bibliotheque import settings

urlpatterns = [
    path('', index, name='index'),
    path('liste/', liste, name='liste'),
    path('livre/<int:id>', livre_detail, name='livre_detail'),
    path('telechargement-livre/<int:id>', telechargement_livre, name='telechargement_livre'),
    path('recherche/', recherche_livre, name='recherche_livre'),
    path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
