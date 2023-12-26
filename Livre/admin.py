from django.contrib import admin
from Livre.models import Livre
from django.utils.translation import gettext_lazy as _

# importena eto lay base des données mba hahafahana mi'gerer azy any @ espace admin

admin.site.register(Livre)


#parametre django admin
admin.site.site_title = _("GESTION DE BIBLIOTHEQUE")
admin.site.site_header = _("GESTION DE BIBLIOTHEQUE")
admin.site.index_title = _("GESTION DE BIBLIOTHEQUE")
