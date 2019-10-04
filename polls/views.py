from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from .forms import SalvarIten
from django.http import HttpResponse
from .models import Restaurante

from meusite.forms import mapForm
# Create your views here.

def menu(request):
    return render(request,'menu/index.html')

def salvar_dados(request):
    if request.method == "POST":
        form = SalvarIten(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            
    elif(request.method == 'GET'):
        return render(request, 'polls/cadastrarCardapio.html', {'form': form})

def home(request):
 
    # Cria form
    form = mapForm(request.POST or None)   
 
    # Valida e salva
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")
 
    # Chama Template
    return render_to_response("mapa.html",
                              locals(),
                              context_instance = RequestContext(request))