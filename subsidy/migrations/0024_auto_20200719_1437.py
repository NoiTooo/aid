# Generated by Django 3.0.3 on 2020-07-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy', '0023_auto_20200710_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsidy',
            name='maximum_support_amount',
        ),
        migrations.RemoveField(
            model_name='subsidy',
            name='overview',
        ),
        migrations.RemoveField(
            model_name='subsidy',
            name='target',
        ),
        migrations.AddField(
            model_name='subsidy',
            name='condition_img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='支給条件イメージ'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='description_img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='支援内容イメージ'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='how_to_apply_img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='利用・申請方法イメージ'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='supplies',
            field=models.TextField(blank=True, null=True, verbose_name='支給品'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='supplies_img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='支給品イメージ'),
        ),
        migrations.AddField(
            model_name='subsidy',
            name='support_img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='助成額イメージ'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='condition',
            field=models.TextField(verbose_name='支給条件'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='description',
            field=models.TextField(verbose_name='支援内容'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='how_to_apply',
            field=models.TextField(blank=True, null=True, verbose_name='利用・申請方法'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='prefecture',
            field=models.CharField(max_length=10, verbose_name='都道府県(ex.東京都or全国)'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='support_amount_note',
            field=models.TextField(blank=True, null=True, verbose_name='助成額'),
        ),
    ]
