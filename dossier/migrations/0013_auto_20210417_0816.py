# Generated by Django 3.1.5 on 2021-04-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0012_auto_20210417_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossier',
            name='category',
        ),
        migrations.AddField(
            model_name='dossier',
            name='category',
            field=models.ManyToManyField(blank=True, to='dossier.Category'),
        ),
    ]
