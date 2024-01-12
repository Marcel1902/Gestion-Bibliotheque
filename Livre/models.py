from django.db import models

# Eto no mamorona ny modele base des données

class Livre(models.Model):
    Titre = models.CharField(max_length=128)
    Auteur = models.CharField(max_length=128)
    id = models.AutoField(primary_key=True)
    Date_de_production = models.DateField(blank=True)
    Adresse = models.CharField(max_length=128)
    Mot_cle = models.CharField(max_length=128)
    Format = models.CharField(max_length=128)
    NB_PAGES = models.IntegerField(default=1)
    Categorie = models.CharField(max_length=128)
    Note_resume = models.TextField(blank=True)
    Couverture = models.ImageField(upload_to="media")
    Fichier = models.FileField(upload_to="media")
    
    
    def __str__(self):
        return self.Titre