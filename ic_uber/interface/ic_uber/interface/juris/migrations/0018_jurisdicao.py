# Generated by Django 3.1.5 on 2021-02-02 21:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0017_auto_20210202_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisdicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Cadastre as Jurisdições', max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(5, 'Este campo deve possuir mais que 5 caracteres.')])),
                ('vara', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='juris.varas')),
            ],
        ),
    ]
