# Generated by Django 3.0.4 on 2020-03-23 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200323_2120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='APIToken',
            new_name='Token',
        ),
    ]
