# Generated by Django 4.2.7 on 2023-11-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_alter_parceria_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoafisica',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='pessoafisica',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='pessoajuridica',
            name='nome',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=32, null=True),
        ),
    ]