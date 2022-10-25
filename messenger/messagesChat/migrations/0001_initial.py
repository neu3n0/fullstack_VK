# Generated by Django 4.1.2 on 2022-10-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('pub_data', models.DateTimeField(auto_now_add=True)),
                ('is_readed', models.BooleanField(default=False)),
            ],
        ),
    ]