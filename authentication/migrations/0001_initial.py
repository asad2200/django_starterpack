# Generated by Django 3.2.4 on 2021-06-28 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForgotPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('code', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verifiaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('code', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
    ]
