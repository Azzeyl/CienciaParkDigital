# Generated by Django 4.2.6 on 2023-11-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primerNombre', models.CharField(max_length=50)),
                ('segundoNombre', models.CharField(max_length=50)),
                ('primerApellido', models.CharField(max_length=50)),
                ('segundoApellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('nivelEscolar', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
