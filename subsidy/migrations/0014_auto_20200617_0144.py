# Generated by Django 3.0.7 on 2020-06-16 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsidy', '0013_auto_20200615_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_found', models.CharField(choices=[('1', '-----'), ('2', 'URLのリンクが切れている'), ('3', '内容が誤っている')], max_length=100, verbose_name='問題')),
                ('applicable_url', models.CharField(max_length=1000, verbose_name='該当URL')),
                ('response_completed', models.BooleanField(blank=True, null=True, verbose_name='対応完了')),
                ('response_note', models.CharField(blank=True, max_length=300, null=True, verbose_name='対応メモ')),
            ],
            options={
                'verbose_name': '05.お問合せ',
                'verbose_name_plural': '05.お問合せ',
            },
        ),
        migrations.AddField(
            model_name='subsidy',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='公開'),
            preserve_default=False,
        ),
    ]
