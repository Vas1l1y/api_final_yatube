# Generated by Django 2.2.16 on 2022-09-14 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
