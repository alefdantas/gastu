"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from  ppi import settings
from . import views
app_name = 'polls'

urlpatterns = [
   
    path('cadastro/', views.cadastro_de_cardapio, name='cadastro_de_cardapio'),
    path('exibir/', views.exibirCardapio, name='exibirCardapio'),
    path('localizacao/', views.mapView, name='mapa'),
    path('update/<int:pk>/', views.update_cardapio, name='update_cardapio'),
    path('delete/<int:pk>/', views.delete_cardapio, name='delete_cardapio'),
    path('base/', views.base_metodo, name='base_metodo'),

   
]