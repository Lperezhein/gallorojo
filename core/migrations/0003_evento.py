# Generated by Django 4.2.7 on 2025-02-23 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_noticia_contenido_alter_noticia_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
