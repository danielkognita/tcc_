# Generated by Django 3.2.7 on 2022-08-17 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_experimento_id_experimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experimento',
            name='created_at',
        ),
    ]
