from django.db import models
from django.contrib.auth.models import User


class Cidade(models.Model):
    codigocidade = models.IntegerField(primary_key=True)
    cidade = models.CharField(max_length=75)

class Bairro(models.Model):
    codigobairro = models.IntegerField(primary_key=True)
    bairro = models.CharField(max_length=150)
    
class Restaurante(models.Model):
    cnpj = models.CharField(max_length=10,primary_key=True)
    nome = models.CharField(max_length=200)
    nome_comercial = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    
class Pessoa(models.Model):
    cpf = models.CharField(max_length=200, primary_key=True)
    data_nascimento = models.DateField()
    nome = models.CharField(max_length=20)
   
    
class Usuario(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=20, primary_key=True)
    senha = models.CharField(max_length=16)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default=None)
    
class Pedido(models.Model):
    endereco = models.CharField(max_length=100)
    valor_final = models.CharField(max_length=10)
    status = models.CharField(max_length=25)
    codigopedido = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)
    

class Prato(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=35)
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    disponibilidade = models.CharField(max_length=25)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=None)

class Itens(models.Model):
    
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    disponibilidade = models.CharField(max_length=20)
    valor = models.IntegerField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=None)

