# Generated by Django 4.0.2 on 2022-03-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(blank=True, max_length=10)),
                ('entrada', models.CharField(blank=True, max_length=10)),
                ('usuario', models.CharField(blank=True, max_length=20)),
                ('total', models.CharField(blank=True, max_length=10)),
                ('saida', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
