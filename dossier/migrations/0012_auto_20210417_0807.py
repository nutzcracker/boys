# Generated by Django 3.1.5 on 2021-04-17 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0011_auto_20210415_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='dossier',
        ),
        migrations.AddField(
            model_name='dossier',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dossier.category'),
        ),
    ]
