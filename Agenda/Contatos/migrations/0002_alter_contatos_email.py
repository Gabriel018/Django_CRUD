# Generated by Django 3.2.6 on 2022-04-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatos',
            name='Email',
            field=models.EmailField(max_length=200),
        ),
    ]