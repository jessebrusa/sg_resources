# Generated by Django 5.0.1 on 2024-01-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_transition', '0002_visit_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='date_completed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
