# Generated by Django 3.1.7 on 2021-04-10 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0009_auto_20210410_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='dossier',
            name='props',
        ),
        migrations.AddField(
            model_name='category',
            name='dossier',
            field=models.ManyToManyField(blank=True, to='dossier.Dossier'),
        ),
        migrations.AddField(
            model_name='property',
            name='dossier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dossier.dossier', verbose_name='Досье'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_type',
            field=models.CharField(max_length=200, verbose_name='Категория граждан'),
        ),
    ]
