# Generated by Django 2.1.3 on 2020-01-04 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_db', '0011_triggeractionfilter_parent'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='api',
            index_together={('app', 'model')},
        ),
        migrations.AlterIndexTogether(
            name='trigger',
            index_together={('app', 'model', 'event')},
        ),
    ]