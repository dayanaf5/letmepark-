# Generated by Django 2.2.11 on 2020-03-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EjemploDato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('longitud', models.IntegerField(null=True)),
                ('latitud', models.IntegerField(null=True)),
                ('direccion', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
