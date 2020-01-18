from django.db import models
from django.contrib.auth.models import User


class Cidade(models.Model):
    cidade = models.CharField(max_length=75)

class Bairro(models.Model):
    bairro = models.CharField(max_length=150)
    
class Restaurante(models.Model):
    id_restaurante = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=10)
    nome = models.CharField(max_length=200)
    nome_comercial = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')
    
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    nome = models.CharField(max_length=20)
   
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    senha = models.CharField(max_length=16)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=None)
    
class Pedido(models.Model):
    endereco = models.CharField(max_length=100)
    valor_final = models.CharField(max_length=10)
    status = models.CharField(max_length=25)
    id_pedido = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    

class Prato(models.Model):
    id_prato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=35)
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    disponibilidade = models.CharField(max_length=25)
    foto = models.ImageField(upload_to='media/imagens/')

class Itens(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=20)
    valor = models.IntegerField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=None)

