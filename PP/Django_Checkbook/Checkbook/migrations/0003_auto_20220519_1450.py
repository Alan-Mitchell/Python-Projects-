# Generated by Django 2.1.5 on 2022-05-19 19:50

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0002_auto_20220517_2042'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='transaction',
            managers=[
                ('Transactions', django.db.models.manager.Manager()),
            ],
        ),
    ]
