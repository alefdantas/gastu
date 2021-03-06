# Generated by Django 2.2.6 on 2020-02-12 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=200)),
                ('data_nascimento', models.DateField()),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id_restaurante', models.AutoField(primary_key=True, serialize=False)),
                ('cnpj', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=200)),
                ('nome_comercial', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=16)),
                ('pessoa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id_prato', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=35)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('disponibilidade', models.CharField(max_length=25)),
                ('foto', models.ImageField(upload_to='media/imagens/')),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('endereco', models.CharField(max_length=100)),
                ('valor_final', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=25)),
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
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
