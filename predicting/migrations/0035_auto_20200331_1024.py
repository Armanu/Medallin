# Generated by Django 3.0.4 on 2020-03-31 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0034_auto_20200330_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='triage',
            field=models.CharField(choices=[('low', 'کم\u200cخطر'), ('medium', 'متوسط'), ('high', 'پر\u200cخطر')], max_length=6),
        ),
    ]