# Generated by Django 4.2.7 on 2025-02-23 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='eventos/'),
        ),
    ]
