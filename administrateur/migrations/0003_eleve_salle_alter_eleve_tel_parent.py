# Generated by Django 5.0.7 on 2025-01-20 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0002_matiere_rename_id_enseignant_salle_enseignant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='salle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='eleves', to='administrateur.salle'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eleve',
            name='tel_parent',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
