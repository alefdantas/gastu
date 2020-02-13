from django.urls import path,include
from . import views


app_name = 'gastu'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    
 	path('polls/', include('polls.urls')),
     
]

    