# Generated by Django 2.1.3 on 2020-01-09 10:30

import api_db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0012_auto_20200104_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trigger',
            name='slug',
            field=models.SlugField(default=api_db.models.UUID, unique=True, verbose_name='标识'),
        ),
    ]