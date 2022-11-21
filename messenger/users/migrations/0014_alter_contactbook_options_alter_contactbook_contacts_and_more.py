# Generated by Django 4.1.3 on 2022-11-20 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_contactbook_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactbook',
            options={'verbose_name': 'Контактная книга', 'verbose_name_plural': 'Контактные книги'},
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='contacts',
            field=models.ManyToManyField(related_name='bookcontacts', to=settings.AUTH_USER_MODEL, verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='contactbook',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contactbook', to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
