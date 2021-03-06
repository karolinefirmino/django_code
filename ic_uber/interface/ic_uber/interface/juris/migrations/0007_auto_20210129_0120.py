# Generated by Django 3.1.5 on 2021-01-29 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0006_auto_20210129_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='tipoProcesso',
            field=models.BooleanField(choices=[('Individual', 'Individual'), ('Coletivo', 'Coletivo'), ('Unknown', 'Unknown')], null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='tipoDecisao',
            field=models.BooleanField(choices=[('Decisao', 'Decisao'), ('Sentença', 'Sentença'), ('Acórdão', 'Acórdão')]),
        ),
    ]
