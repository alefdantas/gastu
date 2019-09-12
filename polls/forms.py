from django import forms

from .models import Usuario, Itens

class SalvarLogin(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('latitude', 'longitude','email','username','senha','pessoa')
class SalvarIten(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ('nome', 'descricao', 'disponibilidade','valor')