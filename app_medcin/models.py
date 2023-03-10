from django.db import models
from django.urls import reverse
import uuid
from utilisateur.models import Medcin
from parametres.models import Clinique

# Create your models here.
# # la class de base
# class BaseModel(models.Model):# toutes les autres class vont heriter de ces 3 attributs de la class BaseModel
#     uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
#     status=models.BooleanField(default=True,help_text='active ou desactive')
#     created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
#     updated=models.DateTimeField(auto_now=True,help_text='Update date')

#     class Meta:
#         abstract=True

class Education(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    formation=models.CharField(max_length=255,blank=True,null=True,help_text='Le libelle de la formation')
    ecole=models.CharField(max_length=255,blank=True,null=True,help_text="Le libelle de l'cole")
    description = models.TextField(blank=True,null=True) #Short Description of the Education
    date_debut = models.DateField(blank=True, null=True,help_text='Date de debut de la formation')
    date_fin = models.DateField(blank=True, null=True,help_text='Date de fin de la formation')
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_medcin_education")

    def __str__(self):
        return f'{self.formation} {self.medcin.nom}'

    def get_absolute_url(self):
        return reverse("education_details", kwargs={'pk': self.pk})
    
class Experience(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    poste=models.CharField(max_length=255,blank=True,null=True,help_text='Le libelle du poste occupé')
    clinique = models.ForeignKey(Clinique,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner la clinique',related_name="fk_clinique_experience")
    description = models.TextField(blank=True,null=True) #Short Description of the Experience
    date_debut = models.DateField(blank=True, null=True,help_text='Date de debut de la formation')
    date_fin = models.DateField(blank=True, null=True,help_text='Date de fin de la formation')
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_clinique_experience")

    def __str__(self):
        return f'{self.poste} {self.medcin.nom}'

    def get_absolute_url(self):
        return reverse("experience_details", kwargs={'pk': self.pk})
 
class Certificat(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')
   
    titre=models.CharField(max_length=255,blank=True,null=True,help_text='Le libelle du Certificat')
    description = models.TextField(blank=True,null=True) #Short Description of the Certificat
    date = models.DateField(blank=True, null=True,help_text='Date')
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_Certificat")

    def __str__(self):
        return f'{self.titre} {self.medcin.nom}'

    def get_absolute_url(self):
        return reverse("certificat_details", kwargs={'pk': self.pk})
    
class Galerie(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')
    
    titre=models.CharField(max_length=255,blank=True,null=True,help_text="Le libelle de l'cole")
    photo = models.ImageField(upload_to='medcins/galerie/',blank=True, null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Galerie
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_medcin_galerie")

    def __str__(self):
        return f'{self.titre} {self.medcin.nom}'
    
    def get_absolute_url(self):
        return reverse("galerie_details", kwargs={'pk': self.pk})
    
class Disponibilite(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')
    
    joursDisponibilite=models.CharField(max_length=255,blank=True,null=True,help_text='Les jours de disponibilité')
    tempsDisponibilite=models.CharField(max_length=255,blank=True,null=True,help_text="Temps de disponibilité")
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_medcin_disponibilite")
    description = models.TextField(blank=True,null=True,help_text='Ce champ est ptionnel') #Short Description of the Disponibilite
    
    # lundi
    heure_debut_lundi = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_lundi = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin fin')
    
    # mardi
    heure_debut_mardi = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_mardi = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')
    
    # mercredi
    heure_debut_mercredi = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_mercredi = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')
    
    # jeudi
    heure_debut_jeudi = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_jeudi = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')
    
    # vendredi
    heure_debut_vendredi = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_vendredi = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')
    
    # samedi
    heure_debut_samedi = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_samedi = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')
    
    # dimanche
    heure_debut_dimanche = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin_dimanche = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')

    def __str__(self):
        return f'{self.medcin.nom}'

    def get_absolute_url(self):
        return reverse("disponibilite_details", kwargs={'pk': self.pk})
    
class SpecialisationMedcin(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')
    
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the SpecialisationMedcin
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_SpecialisationMedcin")

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
       return reverse("SpecialisationsMedcin_details", kwargs={'pk': self.pk})

