# Generated by Django 3.0.7 on 2020-06-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy', '0005_auto_20200605_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=30),
        ),
    ]
