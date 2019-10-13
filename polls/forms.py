from django import forms
from django.core.validators import RegexValidator

import re 

# cria objeto Regex
caracteres = RegexValidator(
    # regex= re.compile(r"[a-zA-Z]+"),
    regex=r"[a-zA-Z]+",
    message="Permitido somente caracteres Alpha numericos",
    code="invalid")

from .models import Usuario, Itens, Restaurante

class SalvarLogin(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('latitude', 'longitude','email','username','senha','pessoa')
class SalvarIten(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ('nome', 'descricao', 'disponibilidade','valor')

class mapForm(forms.ModelForm):
    # Associa formulario ao modelo
    class Meta:
        model = Restaurante
        fields = ('latitude', 'longitude')