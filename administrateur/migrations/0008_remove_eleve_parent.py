# Generated by Django 5.0.7 on 2025-03-17 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0007_emploidetemp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='parent',
        ),
    ]
