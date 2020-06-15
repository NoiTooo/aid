# Generated by Django 3.0.3 on 2020-06-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy', '0012_inquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsidy',
            name='maximum_amount',
        ),
        migrations.AddField(
            model_name='subsidy',
            name='maximum_support_amount',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='最大支給額'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='referrer',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='参照元'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='support_amount_note',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='支給額補足'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='target',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='対象'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='condition',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='条件'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='説明文'),
        ),
    ]
