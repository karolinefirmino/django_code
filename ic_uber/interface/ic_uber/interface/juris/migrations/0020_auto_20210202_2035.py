# Generated by Django 3.1.5 on 2021-02-02 23:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0019_auto_20210202_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termobusca',
            name='name',
            field=models.CharField(help_text='Cadastre os termos buscados nas bases de dados', max_length=200, validators=[django.core.validators.MinLengthValidator(4, 'O campo do tribunal deve possuir mais que 4 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='tribunal',
            name='name',
            field=models.CharField(help_text='Cadastre os Tribunais do Trabalho, Tribunal Superior do Trabalho, entre outros (e.g. TRT3)', max_length=200, unique=True),
        ),
    ]
