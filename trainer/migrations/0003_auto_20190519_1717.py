# Generated by Django 2.0.13 on 2019-05-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0002_auto_20190519_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
