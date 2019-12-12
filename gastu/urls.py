from django.urls import path,include
from . import views


app_name = 'gastu'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('/<slug:slug>', views.post_detail, name='post_detail'),
    path('sobre-nos/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('turismo/', views.tourism, name='tourism'),
    path('gastronomia/', views.gastronomy, name='gastronomy'),
    path('rio-grande-do-norte/', views.rn, name='rn'),
    path('ideia/', views.idea, name='idea'),
    path('detail/', views.detail, name='detail'),
 	path('polls/', include('polls.urls')),
     
]

    