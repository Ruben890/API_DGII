# Generated by Django 4.2.6 on 2023-11-01 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIDGII', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rnc',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
