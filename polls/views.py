from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, redirect
from .forms import FormCardapio, mapForm
from django.template import RequestContext
from django.http import HttpResponse
from .models import Restaurante, Prato
from django.conf.urls.static import static

# Create your views here.

def base_metodo(request):
    return render(request,'polls/base3.html')

def menu(request):
    return render(request,'index.html')

def exibirCardapio(request):
    return render(request,'exibirCardapio.html',{'pratos': Prato.objects.all()})

def cadastro_de_cardapio(request):
    form_class = FormCardapio
    form = form_class(request.POST or None)
    user = request.user
    if request.method == "POST":
        form = FormCardapio(request.POST)
        if form.is_valid():
            card = form.save(commit=False)

            card.post = request.user
            card.save()
    else:
        form = FormCardapio()
    return render(request, 'cadastrarCardapio.html', {'form': form})

def update_cardapio(request, pk):
    consulta = Prato.objects.get(pk=pk)
    form = FormCardapio(request.POST or None, instance=consulta)
    if form.is_valid():
        form.save()
        return render(request,'exibirCardapio.html',{'pratos': Prato.objects.all()}) 

def delete_cardapio(request, pk):
    consulta = Prato.objects.get(pk=pk)
    consulta.delete()

def mapView(request):
    restaurantes = Restaurante.objects.all()
    # Cria form
    #form = mapForm(request.POST or None)   
 
    # Valida e salva
    # if form.is_valid():
    #    salvar = form.save(commit=False)
    #    salvar.save()
    #    return HttpResponse("Dados inseridos com sucesso!")
    #
    # Chama Template
    return render(request, "gastu/base2.html" ,{"restaurantes":restaurantes})

