# Generated by Django 2.2 on 2019-08-08 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('codigobairro', models.IntegerField(primary_key=True, serialize=False)),
                ('bairro', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('codigocidade', models.IntegerField(primary_key=True, serialize=False)),
                ('cidade', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('cpf', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('data_nascimento', models.DateField()),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=16)),
                ('pessoa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('cnpj', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('nome_comercial', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nome', models.CharField(max_length=35)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('disponibilidade', models.CharField(max_length=25)),
                ('restaurante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('endereco', models.CharField(max_length=100)),
                ('valor_final', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=25)),
                ('codigopedido', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('disponibilidade', models.CharField(max_length=20)),
                ('valor', models.IntegerField()),
                ('restaurante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Restaurante')),
            ],
        ),
    ]
