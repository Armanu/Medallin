# Generated by Django 3.0.4 on 2020-03-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predicting', '0039_auto_20200331_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='values',
            field=models.CharField(choices=[('[-1, 1]', '[-1, 1]'), ('[0, 1]', '[0, 1]'), ('-1, 0, 1', '-1, 0, 1')], default='[-1, 1]', max_length=16),
            preserve_default=False,
        ),
    ]
