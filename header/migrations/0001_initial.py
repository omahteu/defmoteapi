# Generated by Django 4.0.2 on 2022-02-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabeca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datahora', models.CharField(blank=True, max_length=10)),
                ('valor', models.CharField(blank=True, max_length=10)),
                ('quanrto', models.CharField(blank=True, max_length=2)),
            ],
        ),
    ]
