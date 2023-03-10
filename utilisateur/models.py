from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
import uuid
from PIL import Image
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from taggit.managers import TaggableManager
from parametres.models import Ville,Departement,Specialite,Piece,Profession,Specialisations

class UserProfileManager(BaseUserManager):
    def create_user(self,email,password=None,*callback_args, **callback_kwargs):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email)
        
        user.set_password(password)
        
        # user=self.model(username=username,password=password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        user=self.create_user(email,password)
        
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        
        user.save(using=self._db)
        return user   
    
class CustomUser(AbstractUser):
    GENRES = (
        ('h', 'Homme'),
        ('f', 'Femme'),
    )

    CIVILITES = (
        ('Monsieur','Monsieur'),
        ('Madame','Madame'),
        ('Mademoiselle','Mademoiselle'),
    )
    STATUT_MATRIMONIAL = (
        ('célibataire', 'Célibataire'),
        ('mariée', 'Marié/Mariée'),
        ('veuve', 'Veuf/Veuve'),
        ('divorcée', 'Divorcé/Divorcée'),
        
    )

    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	
    is_medcin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    email = models.EmailField(max_length=254, unique=True)
    username = None

    last_name = models.CharField(max_length=250, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    midle_name = models.CharField(max_length=250, blank=True, null=True)
    
    photo = models.ImageField(upload_to='users/avatar/',blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    date_naissance = models.DateField(blank=True,null=True)
    lieu_naissance = models.CharField(max_length=255,blank=True,null=True)
    
    code_postal = models.CharField(max_length=255,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)

    session_token = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    telephone= PhoneNumberField(null=False, blank=False)
    pays = CountryField(null=True,blank=True,blank_label='(select country)')
    addresse = models.CharField(max_length=255,blank=True,null=True)

    genre = models.CharField(
        max_length=1,
        choices=GENRES,
        blank=True,
        default='h',
        help_text='Select genre',
    )
    statut_matrimonial = models.CharField(
        max_length=100,
        choices=STATUT_MATRIMONIAL,
        blank=True,
        default='célibataire',
        help_text='statut matrimonial',
    )

    civilite = models.CharField(
        max_length=100,
        choices=CIVILITES,
        blank=True,
        default='Monsieur',
        help_text='select civilité',
    )

    ville = models.ForeignKey(Ville,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_medcin_ville")
    piece = models.ForeignKey(Piece,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_medcin_piece")
  
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

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.is_medcin:
                type_ = 'Medcin'
        elif self.is_patient:
            type_ = 'Patient'
        else:
            type_ = 'None'
        return f'{type_}: {self.email}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            pic = Image.open(self.photo.path)
            if pic.width > 256:
                pic.thumbnail((256, pic.height / (pic.width / 265)))
                pic.save(self.photo.path)

    def get_photo_url(self):
        if self.photo:
            return self.photo.url
        else:
            if self.is_medcin:
                return '/media/users/medcin-default.jpg'
            elif self.is_patient:
                return '/media/users/patient-default.jpg'
            else:
                return '/media/users/default.jpg'

    def get_photo_name(self):
        if self.photo:
            return self.photo.name 
        else:
            if self.is_medcin:
                return 'medcin-default.jpg'
            elif self.is_patient:
                return 'patient-default.jpg'
            else:
                return 'default.jpg'

    def get_profile(self):
        if self.is_medcin:
            return Medcin.objects.get(user=self)
        elif self.is_patient:
            return Patient.objects.get(user=self)
        else:
            return None

    def get_shortname(self):
        return f'{self.first_name[0:1]}.{self.last_name}'

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'
        
    objects= UserProfileManager()

# medcin
class Medcin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    IDMedcin = models.CharField(max_length=255,blank=True,null=True,unique=True)
    photo = models.ImageField(upload_to='medcins/profile/',blank=True, null=True)
    signature = models.ImageField(upload_to='medcins/signatures/',blank=True, null=True)
    specialite = models.ForeignKey(Specialite,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_specialite")
    specialisation = models.ManyToManyField(Specialisations,blank=True,null=True,related_name="fk_specialisation")
    departement = models.ForeignKey(Departement,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_departement")
    views = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.email}'

    def get_absolute_url(self):
        return reverse("medcin_details", kwargs={'pk': self.pk})

# patient
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, unique=True)
    IDPatient = models.CharField(max_length=255,blank=True,null=True,unique=True)
    photo = models.ImageField(upload_to='patients/profile/',blank=True, null=True)
    signature = models.ImageField(upload_to='patients/signatures/',blank=True, null=True)
    profession = models.ForeignKey(Profession,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_id_profession")
  
    def __str__(self):
        return f'{self.user.email}'
        # return self.IDPatient

    def get_absolute_url(self):
        return reverse("patient_details", kwargs={'pk': self.pk})

