# Generated by Django 5.0.7 on 2025-02-06 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0012_alter_utilisateur_datecreation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='DateCreation',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 6, 10, 58, 43, 71189)),
        ),
    ]
