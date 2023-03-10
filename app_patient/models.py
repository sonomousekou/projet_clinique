from django.db import models
from django.urls import reverse
import uuid
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from utilisateur.models import Medcin, Patient

# Create your models here.
# RendezVous    
class RendezVous(models.Model):
# Le statut en attente signifie que la tâche n'est pas commencée. ...
# Le statut en cours signifie que la tâche est en train d'être effectuée.
# Le statut complété signifie que la tâche est terminée, fermée. ...

    TYPE_ETAT=(
        ('en attente','En attente'),
        ('en cours','En cours'),
        ('terminé','Terminé'),
    )

    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    status=models.BooleanField(default=True,help_text='active ou desactive')
    created=models.DateField(auto_now_add=True,blank=True,null=True,help_text='Create date')
    updated=models.DateTimeField(auto_now=True,help_text='Update date')

    patient = models.ForeignKey(Patient,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_patient_rendezvous")
    medcin = models.ForeignKey(Medcin,on_delete=models.SET_NULL,blank=True,null=True,related_name="fk_medcin_rendezvous")
    date = models.DateField(blank=True,null=True)
    heure_debut = models.TimeField(blank=True, null=True,help_text='Heure de debut')
    heure_fin = models.TimeField(blank=True, null=True,help_text='Heure de fin de fin')
    etat = models.CharField(
        max_length=50,
        choices=TYPE_ETAT,
        blank=True,
        default='en attente',
        help_text='Select etat',
    )
    prix = MoneyField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinMoneyValidator(10),
            MaxMoneyValidator(1500),
            # MinMoneyValidator(Money(500, 'NOK')),
            # MaxMoneyValidator(Money(900, 'NOK')),
            # MinMoneyValidator({'EUR': 100, 'USD': 50}),
            # MaxMoneyValidator({'EUR': 1000, 'USD': 500}),
        ],
    )

    def __str__(self):
        return f'{self.patient.nom} '

    def get_absolute_url(self):
        return reverse("rendezvous_details", kwargs={'pk': self.pk})
