# Generated by Django 5.0.1 on 2024-01-18 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_transition', '0004_remove_device_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='reccomendation',
            new_name='recommendation',
        ),
    ]
