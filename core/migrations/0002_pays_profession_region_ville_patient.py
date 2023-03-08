# Generated by Django 4.1.7 on 2023-03-08 09:06

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('libelle', django_countries.fields.CountryField(blank=True, max_length=2, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('libelle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('libelle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('libelle', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, help_text='active ou desactive')),
                ('created', models.DateField(auto_now_add=True, help_text='Create date', null=True)),
                ('updated', models.DateTimeField(auto_now=True, help_text='Update date')),
                ('IDPatient', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, choices=[('h', 'Homme'), ('f', 'Femme')], default='h', help_text='Select genre', max_length=1)),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('code_postal', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, help_text='Twitter', max_length=200, null=True)),
                ('facebook', models.CharField(blank=True, help_text='Facebook', max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, help_text='Instagram', max_length=200, null=True)),
                ('linkdin', models.CharField(blank=True, help_text='Linkdin', max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='patients/avatar/')),
                ('pays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_pays', to='core.pays')),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_profession', to='core.profession')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_region', to='core.region')),
                ('ville', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_ville', to='core.ville')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
