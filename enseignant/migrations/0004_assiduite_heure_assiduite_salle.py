# Generated by Django 5.0.7 on 2025-02-27 12:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0005_matiere_niveau_salle_niveau'),
        ('enseignant', '0003_rename_matiere_enseignant_matiere_enseignee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assiduite',
            name='heure',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='assiduite',
            name='salle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrateur.salle'),
            preserve_default=False,
        ),
    ]
