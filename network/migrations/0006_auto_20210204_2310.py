# Generated by Django 3.1.5 on 2021-02-04 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20210131_1757'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follower',
            new_name='Following',
        ),
    ]