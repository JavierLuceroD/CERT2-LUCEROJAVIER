# Generated by Django 4.2.6 on 2023-10-23 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docente',
            name='carrera',
        ),
        migrations.DeleteModel(
            name='Carrera',
        ),
        migrations.DeleteModel(
            name='Docente',
        ),
    ]
