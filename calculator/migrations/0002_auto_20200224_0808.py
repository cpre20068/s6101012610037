# Generated by Django 3.0.3 on 2020-02-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calc',
            name='operations',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='calc',
            name='x',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='calc',
            name='y',
            field=models.IntegerField(blank=True),
        ),
    ]
