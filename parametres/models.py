from django.db import models
from django.urls import reverse
import uuid
from django_countries.fields import CountryField

# Create your models here.
class Specialite(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Specialite
    image = models.ImageField(upload_to='specialites') #Cover Image of the Specialite

    # Meta data
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Specialite'
        
    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("specialite_details", kwargs={'pk': self.pk})

class Departement(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Departement
    image = models.ImageField(upload_to='departements') #Cover Image of the Departement

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("departement_details", kwargs={'pk': self.pk})
        
class Ecole(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Ecole

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("ecole_details", kwargs={'pk': self.pk})
    
class Formation(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Formation

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("formation_details", kwargs={'pk': self.pk})

#   les champs d'action des medcins  
class Specialisations(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Specialisations

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("Specialisations_details", kwargs={'pk': self.pk})
  
class Clinique(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Clinique

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("clinique_details", kwargs={'pk': self.pk})

class Pays(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    libelle = CountryField(null=True,blank=True,blank_label='(select country)',unique=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Pays
    nationnalite = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("pays_details", kwargs={'pk': self.pk})
    
class Region(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    pays = models.ForeignKey(Pays,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_pays")
    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    libelle = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Region

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("region_details", kwargs={'pk': self.pk})
    
class Ville(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    region = models.ForeignKey(Region,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_region")
    code=models.CharField(max_length=255,blank=True,null=True,unique=True)
    libelle=models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Ville

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("ville_details", kwargs={'pk': self.pk})
    
class Profession(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    libelle = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True) #Short Description of the Profession

    def __str__(self):
        return self.libelle

    def get_absolute_url(self):
        return reverse("profession_details", kwargs={'pk': self.pk})
    
class Type_Piece(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    libelle = models.CharField(max_length=255,blank=True,null=True,unique=True)
    format = models.CharField(max_length=255,blank=True,null=True,unique=True)
    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    
    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("type_piece_details", kwargs={'pk': self.pk})

class Piece(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    date_etablissement = models.CharField(max_length=255,blank=True,null=True,unique=True)
    date_expiration = models.CharField(max_length=255,blank=True,null=True,unique=True)
    lieu_etablissemnt = models.CharField(max_length=255,blank=True,null=True,unique=True)
    numero_piece = models.CharField(max_length=255,blank=True,null=True,unique=True)
    type_piece = models.ForeignKey(Type_Piece,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_type_piece")
   
    def __str__(self):
        return self.numero_piece

    def get_absolute_url(self):
        return reverse("piece_details", kwargs={'pk': self.pk})

