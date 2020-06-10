# Generated by Django 3.0.7 on 2020-06-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy', '0007_auto_20200605_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=30, verbose_name='イベントタグ')),
            ],
            options={
                'verbose_name': '04.イベントタグ',
                'verbose_name_plural': '04.イベントタグ',
            },
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='cities',
            field=models.ManyToManyField(blank=True, to='subsidy.City', verbose_name='市区町村タグ'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='prefectures',
            field=models.ManyToManyField(blank=True, to='subsidy.Prefecture', verbose_name='都道府県タグ'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='events',
            field=models.ManyToManyField(blank=True, to='subsidy.Event', verbose_name='イベントタグ'),
        ),
    ]
