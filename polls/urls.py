from django.urls import path,include
from  ppi import settings
from . import views
app_name = 'polls'

urlpatterns = [
   	path('cadastrorestaurante/', views.cadastro_de_restaurante, name='cadastro_de_restaurante'),
    path('cadastrocardapio/', views.cadastro_de_cardapio, name='cadastro_de_cardapio'),
    path('exibircardapio/', views.exibirCardapio, name='exibirCardapio'),
    path('exibirrestaurante/', views.exibirRestaurante, name='exibirRestaurante'),
    #path('localizacao/', views.mapView, name='mapa'),
    path('updaterestaurante/<int:pk>/', views.update_restaurante, name='update_restaurante'),
    path('updatecardapio/<int:pk>/', views.update_cardapio, name='update_cardapio'),
    path('deletecardapio/<int:pk>/', views.delete_cardapio, name='delete_cardapio'),
    path('base/', views.base_metodo, name='base_metodo'),

]