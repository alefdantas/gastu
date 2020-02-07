from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import Usuario, Prato, Restaurante, Itens
import re 

# cria objeto Regex
caracteres = RegexValidator(
    # regex= re.compile(r"[a-zA-Z]+"),
    regex=r"[a-zA-Z]+",
    message="Permitido somente caracteres Alpha numericos",
    code="invalid")



class SalvarLogin(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('latitude', 'longitude','email','username','senha','pessoa')

class FormCardapio(ModelForm):

    class Meta:
        model = Prato
        fields = ['nome', 'descricao','valor','disponibilidade', 'foto']
        
class mapForm(forms.ModelForm):
    # Associa formulario ao modelo
    class Meta:
        model = Usuario
        fields = ('latitude', 'longitude')

class FormRestaurante(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['cnpj', 'nome','nome_comercial','descricao', 'bairro', 'cidade','imagem']