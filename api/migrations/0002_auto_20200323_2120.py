# Generated by Django 3.0.4 on 2020-03-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apitoken',
            name='token',
            field=models.CharField(blank=True, help_text='Generated automatically.', max_length=64, null=True, unique=True, verbose_name='Token'),
        ),
    ]