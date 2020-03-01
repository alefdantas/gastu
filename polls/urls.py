from django.urls import path,include
from  ppi import settings
from . import views
app_name = 'polls'

urlpatterns = [
    path('user/', views.adminRestaurante, name='adminRestaurante'),
   	path('cadastrorestaurante/', views.cadastro_de_restaurante, name='cadastro_de_restaurante'),
    path('cadastrocardapio/', views.cadastro_de_cardapio, name='cadastro_de_cardapio'),
    path('exibircardapio/', views.exibeCarda, name='exibircardapio'),
    path('exibirrestaurante/', views.exibirRestaurante, name='exibirRestaurante'),
    #path('localizacao/', views.mapView, name='mapa'),
    path('updaterestaurante/<int:pk>/', views.update_restaurante, name='update_restaurante'),
    path('updatecardapio/<int:pk>/', views.update_cardapio, name='update_cardapio'),
    path('deletarrestaurante/<int:pk>/', views.deletar_restaurante, name='deletar_restaurante'),
    path('deletarcardapio/<int:pk>/', views.deletar_cardapio, name='deletar_cardapio'),
    path('base/', views.base_metodo, name='base_metodo'),

]