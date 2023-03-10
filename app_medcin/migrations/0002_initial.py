# Generated by Django 4.1.7 on 2023-03-10 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilisateur', '0001_initial'),
        ('parametres', '0001_initial'),
        ('app_medcin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialisationmedcin',
            name='medcin',
            field=models.ForeignKey(blank=True, help_text='Selectionner le medcin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_SpecialisationMedcin', to='utilisateur.medcin'),
        ),
        migrations.AddField(
            model_name='galerie',
            name='medcin',
            field=models.ForeignKey(blank=True, help_text='Selectionner le medcin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_medcin_galerie', to='utilisateur.medcin'),
        ),
        migrations.AddField(
            model_name='experience',
            name='clinique',
            field=models.ForeignKey(blank=True, help_text='Selectionner la clinique', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_clinique_experience', to='parametres.clinique'),
        ),
        migrations.AddField(
            model_name='experience',
            name='medcin',
            field=models.ForeignKey(blank=True, help_text='Selectionner le medcin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_clinique_experience', to='utilisateur.medcin'),
        ),
        migrations.AddField(
            model_name='education',
            name='medcin',
            field=models.ForeignKey(blank=True, help_text='Selectionner le medcin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_medcin_education', to='utilisateur.medcin'),
        ),
        migrations.AddField(
            model_name='disponibilite',
            name='medcin',
            field=models.ForeignKey(blank=True, help_text='Selectionner le medcin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_medcin_disponibilite', to='utilisateur.medcin'),
        ),
        migrations.AddField(
            model_name='certificat',
            name='medcin',
            field=models.ForeignKey(blank=True, help_text='Selectionner le medcin', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_Certificat', to='utilisateur.medcin'),
        ),
    ]