# Generated by Django 3.1.7 on 2021-04-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0006_auto_20210409_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['name'], 'verbose_name': 'Экипировка', 'verbose_name_plural': 'Экипировки'},
        ),
        migrations.RemoveField(
            model_name='dossier',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat',
        ),
        migrations.AddField(
            model_name='category',
            name='cat',
            field=models.ManyToManyField(null=True, to='dossier.Dossier', verbose_name='Категория граждан'),
        ),
    ]
