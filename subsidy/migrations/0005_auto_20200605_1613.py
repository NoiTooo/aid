# Generated by Django 3.0.7 on 2020-06-05 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy', '0004_auto_20200605_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': '03.市区町村タグ', 'verbose_name_plural': '03.市区町村タグ'},
        ),
        migrations.AlterModelOptions(
            name='prefecture',
            options={'verbose_name': '02.都道府県タグ', 'verbose_name_plural': '02.都道府県タグ'},
        ),
        migrations.AlterModelOptions(
            name='subsidy',
            options={'verbose_name': '01.支援金', 'verbose_name_plural': '01.支援金'},
        ),
    ]
