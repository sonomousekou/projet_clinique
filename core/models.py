from django.db import models
from django.urls import reverse
import uuid
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager

# Create your models here.

# la class de base

class BaseModel(models.Model):# toutes les autres class vont heriter de ces 3 attributs de la class BaseModel
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    class Meta:
        abstract=True

class Specialite(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Specialite
    image = models.ImageField(upload_to='specialites') #Cover Image of the Specialite

    # Metadata
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Specialite'
        
    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("specialite_details", kwargs={'pk': self.pk})

class Departement(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Departement
    image = models.ImageField(upload_to='departements') #Cover Image of the Departement

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("departement_details", kwargs={'pk': self.pk})
        
class Ecole(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Ecole

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("ecole_details", kwargs={'pk': self.pk})
    
class Formation(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Formation

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("formation_details", kwargs={'pk': self.pk})

#   les champs d'action des medcins  
class Specialisations(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Specialisations

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("Specialisations_details", kwargs={'pk': self.pk})
  
class Clinique(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Clinique

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("clinique_details", kwargs={'pk': self.pk})


class Medcin(BaseModel):

    GENRES = (
        ('h', 'Homme'),
        ('f', 'Femme'),
    )

    IDMedcin = models.CharField(max_length=255,blank=True,null=True,unique=True)
    nom = models.CharField(max_length=255,blank=True,null=True)
    prenom = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(db_index=True, unique=True)
    photo = models.ImageField(upload_to='medcins/avatar/',blank=True, null=True)
    telephone = PhoneNumberField(null=False, blank=False, unique=True)
    pays = CountryField(null=True,blank=True,blank_label='(select country)')
    adresse = models.CharField(max_length=255,blank=True,null=True)
    bio = models.TextField(blank=True,null=True) #Short Description of the Specialite
    anniversaire = models.CharField(max_length=255,blank=True,null=True)
    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        blank=True,
        default='h',
        help_text='Select genre',
    )
    tags = TaggableManager()
    specialite=models.ForeignKey(Specialite,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_specialite")
    departement=models.ForeignKey(Departement,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_departement")
    views = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)

    # media social
    twitter = models.CharField(
	    blank=True, null=True, name='twitter', help_text="Twitter", max_length=200)
    facebook = models.CharField(
	    blank=True, null=True, name='facebook', help_text="Facebook", max_length=200)
    instagram = models.CharField(
	    blank=True, null=True, name='instagram', help_text="Instagram", max_length=200)
    linkdin = models.CharField(
	    blank=True, null=True, name='linkdin', help_text="Linkdin", max_length=200)
    youtube = models.CharField(
	    blank=True, null=True, name='youtube', help_text="Linkdin", max_length=200)
    

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("medcin_details", kwargs={'pk': self.pk})
    
    def get_shortname(self):
        return f'{self.prenom[0:1]}.{self.nom}'

    def get_fullname(self):
	    return f'{self.prenom} {self.nom}'

class Education(BaseModel):
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
    
class Experience(BaseModel):
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
    
class Certificat(BaseModel):
    titre=models.CharField(max_length=255,blank=True,null=True,help_text='Le libelle du Certificat')
    description = models.TextField(blank=True,null=True) #Short Description of the Certificat
    date = models.DateField(blank=True, null=True,help_text='Date')
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_Certificat")

    def __str__(self):
        return f'{self.titre} {self.medcin.nom}'

    def get_absolute_url(self):
        return reverse("certificat_details", kwargs={'pk': self.pk})
    
class Galerie(BaseModel):
    titre=models.CharField(max_length=255,blank=True,null=True,help_text="Le libelle de l'cole")
    photo = models.ImageField(upload_to='medcins/galerie/',blank=True, null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Galerie
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_medcin_galerie")

    def __str__(self):
        return f'{self.titre} {self.medcin.nom}'
    
    def get_absolute_url(self):
        return reverse("galerie_details", kwargs={'pk': self.pk})
    
class Disponibilite(BaseModel):
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
    
class SpecialisationMedcin(BaseModel):
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the SpecialisationMedcin
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,help_text='Selectionner le medcin',related_name="fk_SpecialisationMedcin")

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("SpecialisationsMedcin_details", kwargs={'pk': self.pk})
    