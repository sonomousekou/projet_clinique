# Generated by Django 4.1.7 on 2023-03-09 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_type_piece_rename_adresse_medcin_addresse_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='id_type_piece',
            new_name='type_piece',
        ),
    ]