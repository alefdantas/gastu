# Generated by Django 2.2.6 on 2019-10-31 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='imagem',
            field=models.ImageField(default=11, upload_to='imagens/'),
            preserve_default=False,
        ),
    ]
