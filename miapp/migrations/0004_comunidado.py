# Generated by Django 4.2.6 on 2023-10-23 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('detalle', models.CharField(max_length=100)),
                ('detalle_corto', models.CharField(max_length=30)),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.entidad')),
            ],
        ),
    ]