# Generated by Django 5.0.4 on 2024-05-03 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone',
        ),
    ]