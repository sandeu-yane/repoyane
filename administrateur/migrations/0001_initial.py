# Generated by Django 5.0.7 on 2024-09-08 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enseignant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noms', models.CharField(max_length=100)),
                ('prenoms', models.CharField(max_length=100)),
                ('sexe', models.CharField(max_length=10)),
                ('date_naissance', models.DateField()),
                ('quartier', models.CharField(max_length=255)),
                ('classe', models.CharField(max_length=50)),
                ('tel_parent', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('localisation', models.CharField(max_length=255)),
                ('effectifs', models.IntegerField(blank=True, null=True)),
                ('Id_eleve', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salles', to='administrateur.eleve')),
                ('Id_enseignant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salles', to='enseignant.enseignant')),
            ],
        ),
    ]
