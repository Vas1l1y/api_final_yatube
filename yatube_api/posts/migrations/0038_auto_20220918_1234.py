# Generated by Django 2.2.16 on 2022-09-18 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0037_auto_20220918_1231'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_to_following_follow',
        ),
    ]
