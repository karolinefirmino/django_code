# Generated by Django 3.1.5 on 2021-01-29 04:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0010_auto_20210129_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(help_text='O CNPJ dee conter 14 números.', max_length=18, validators=[django.core.validators.MinLengthValidator(14, 'O CNPJ deve conter 14 números')]),
        ),
    ]
