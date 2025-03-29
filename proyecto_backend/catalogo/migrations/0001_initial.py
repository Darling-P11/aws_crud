# Generated by Django 5.1.7 on 2025-03-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_detectado', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('archivo', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
