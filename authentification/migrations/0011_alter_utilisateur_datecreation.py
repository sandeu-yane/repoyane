# Generated by Django 5.0.7 on 2025-02-06 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0010_alter_utilisateur_datecreation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='DateCreation',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 6, 10, 39, 59, 282130)),
        ),
    ]
