# Generated by Django 2.1.3 on 2020-01-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('api_db', '0012_auto_20200104_2158')]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='disable',
            field=models.BooleanField(default=False, verbose_name='停用'),
        )
    ]
