# Generated by Django 4.1.3 on 2022-11-01 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagesChat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['pub_date']},
        ),
    ]