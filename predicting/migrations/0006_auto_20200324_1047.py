# Generated by Django 3.0.4 on 2020-03-24 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0005_auto_20200324_1037'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('concept', 'locale')},
        ),
    ]
