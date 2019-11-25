from django.contrib import admin
from .models import Restaurante
from .models import Usuario
from .models import Pessoa
from .models import Prato
from .models import Pedido
from .models import Bairro
from .models import Cidade
from .models import Itens

# Register your models here.
@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ['id_restaurante','cnpj','nome','nome_comercial','descricao','bairro','cidade','latitude','longitude','imagem']
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id_usuario','latitude','longitude','email','username','senha']
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['id_pessoa','cpf','data_nascimento','nome']
@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ['id_prato','foto','nome','descricao','valor','disponibilidade']
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id_pedido','endereco','valor_final','status']

@admin.register(Itens)
class ItensAdmin(admin.ModelAdmin):
    list_display = ['nome','descricao','disponibilidade','valor']

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['cidade']

@admin.register(Bairro)
class BairroAdmin(admin.ModelAdmin):
    list_display = ['bairro']





