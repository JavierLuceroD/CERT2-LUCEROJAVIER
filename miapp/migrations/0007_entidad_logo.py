# Generated by Django 4.2.6 on 2023-10-23 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0006_comunicado_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos'),
        ),
    ]
