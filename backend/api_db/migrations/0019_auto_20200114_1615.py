# Generated by Django 2.1.3 on 2020-01-14 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0018_auto_20200114_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triggercondition',
            name='trigger',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_db.Trigger', verbose_name='condition'),
        ),
    ]
