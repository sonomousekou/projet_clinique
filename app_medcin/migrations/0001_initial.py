# Generated by Django 4.1.7 on 2023-03-10 14:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificat',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('titre', models.CharField(blank=True, help_text='Le libelle du Certificat', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, help_text='Date', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilite',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('joursDisponibilite', models.CharField(blank=True, help_text='Les jours de disponibilité', max_length=255, null=True)),
                ('tempsDisponibilite', models.CharField(blank=True, help_text='Temps de disponibilité', max_length=255, null=True)),
                ('description', models.TextField(blank=True, help_text='Ce champ est ptionnel', null=True)),
                ('heure_debut_lundi', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_lundi', models.TimeField(blank=True, help_text='Heure de fin de fin fin', null=True)),
                ('heure_debut_mardi', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_mardi', models.TimeField(blank=True, help_text='Heure de fin de fin', null=True)),
                ('heure_debut_mercredi', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_mercredi', models.TimeField(blank=True, help_text='Heure de fin de fin', null=True)),
                ('heure_debut_jeudi', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_jeudi', models.TimeField(blank=True, help_text='Heure de fin de fin', null=True)),
                ('heure_debut_vendredi', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_vendredi', models.TimeField(blank=True, help_text='Heure de fin de fin', null=True)),
                ('heure_debut_samedi', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_samedi', models.TimeField(blank=True, help_text='Heure de fin de fin', null=True)),
                ('heure_debut_dimanche', models.TimeField(blank=True, help_text='Heure de debut', null=True)),
                ('heure_fin_dimanche', models.TimeField(blank=True, help_text='Heure de fin de fin', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('formation', models.CharField(blank=True, help_text='Le libelle de la formation', max_length=255, null=True)),
                ('ecole', models.CharField(blank=True, help_text="Le libelle de l'cole", max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_debut', models.DateField(blank=True, help_text='Date de debut de la formation', null=True)),
                ('date_fin', models.DateField(blank=True, help_text='Date de fin de la formation', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('poste', models.CharField(blank=True, help_text='Le libelle du poste occupé', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_debut', models.DateField(blank=True, help_text='Date de debut de la formation', null=True)),
                ('date_fin', models.DateField(blank=True, help_text='Date de fin de la formation', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Galerie',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('titre', models.CharField(blank=True, help_text="Le libelle de l'cole", max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='medcins/galerie/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialisationMedcin',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('libelle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]