# Generated by Django 3.1.5 on 2021-02-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0014_auto_20210131_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='', verbose_name='processos/pdf')),
            ],
        ),
    ]
