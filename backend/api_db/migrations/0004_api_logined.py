# Generated by Django 2.1.3 on 2019-12-11 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0003_auto_20191210_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='logined',
            field=models.BooleanField(default=True, verbose_name='要求登录'),
        ),
    ]