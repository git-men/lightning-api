# Generated by Django 2.2.17 on 2021-02-03 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0024_auto_20210203_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionparameter',
            name='ref',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='模型'),
        ),
        migrations.AlterField(
            model_name='functionparameter',
            name='type',
            field=models.CharField(choices=[('string', '字符串'), ('int', '整数'), ('decimal', '浮点数'), ('boolean', '布尔值'), ('ref', '数据')], max_length=20, verbose_name='类型'),
        ),
    ]
