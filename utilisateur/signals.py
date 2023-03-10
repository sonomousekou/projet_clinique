from django.db.models.signals import post_save
from .models import CustomUser,Medcin,Patient
from django.dispatch import receiver


def save_profile(sender, instance, created, **kwargs):
	if created:
		if instance.is_medcin:
			medcin = Medcin(user=instance)
			medcin.save()
		elif instance.is_patient:
			patient = Patient(user=instance)
			patient.save()

post_save.connect(save_profile, sender=CustomUser)