# Generated by Django 3.1.7 on 2021-04-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0008_auto_20210410_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dossier',
            old_name='prop',
            new_name='props',
        ),
        migrations.AlterField(
            model_name='category',
            name='cat',
            field=models.ManyToManyField(blank=True, to='dossier.Dossier', verbose_name='Категория граждан'),
        ),
    ]
