# Generated by Django 4.1.3 on 2022-11-19 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_contactbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactbook',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contactbook', to=settings.AUTH_USER_MODEL),
        ),
    ]
