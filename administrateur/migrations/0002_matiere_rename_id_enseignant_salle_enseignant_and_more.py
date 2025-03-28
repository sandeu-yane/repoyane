# Generated by Django 5.0.7 on 2024-12-31 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='salle',
            old_name='Id_enseignant',
            new_name='enseignant',
        ),
        migrations.RemoveField(
            model_name='salle',
            name='Id_eleve',
        ),
        migrations.CreateModel(
            name='Coefficient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coefficient', models.FloatField()),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrateur.salle')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrateur.matiere')),
            ],
        ),
    ]
