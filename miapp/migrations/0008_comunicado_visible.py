# Generated by Django 4.2.6 on 2023-10-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0007_entidad_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
