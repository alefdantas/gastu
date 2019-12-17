from django.urls import path,include
from  ppi import settings
from . import views
app_name = 'polls'

urlpatterns = [
   
    path('cadastro/', views.cadastro_de_cardapio, name='cadastro_de_cardapio'),
    path('exibir/', views.exibirCardapio, name='exibirCardapio'),
    #path('localizacao/', views.mapView, name='mapa'),
    path('update/<int:pk>/', views.update_cardapio, name='update_cardapio'),
    path('delete/<int:pk>/', views.delete_cardapio, name='delete_cardapio'),
    path('base/', views.base_metodo, name='base_metodo'),

]