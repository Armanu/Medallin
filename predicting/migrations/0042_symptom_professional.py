# Generated by Django 3.0.4 on 2020-04-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0041_auto_20200331_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='professional',
            field=models.BooleanField(default=False, verbose_name='Professional'),
        ),
    ]
