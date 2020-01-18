from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, redirect
from .forms import FormCardapio, mapForm
from django.template import RequestContext
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Restaurante, Prato
from django.conf.urls.static import static

# Create your views here.

def base_metodo(request):
    return render(request,'base3.html')

def menu(request):
    return render(request,'index.html')

def exibirCardapio(request):
    exibir = Prato.objects.all().order_by('-created_at')
    return render(request,'exibirCardapio.html', {'pratos': Prato.objects.all()})

def cadastro_de_cardapio(request):
    form = FormCardapio()
    user = request.user

    if request.method == 'POST':
        form = FormCardapio(request.POST)
        if form.is_valid():
            post_foto = form.cleaned_data['foto']
            post_nome = form.cleaned_data['nome']
            post_descricao = form.cleaned_data['descricao']
            post_valor = form.cleaned_data['valor']
            post_disponibilidade = form.cleaned_data['disponibilidade']
            card = form.save(commit=False)

            new_post = Post(foto=post_foto, nome=post_nome, descricao=post_descricao, valor=post_valor, disponibilidade=post_disponibilidade)
            card.post = request.user
            card.save()

            return redirect('cadastro_de_cardapio')

    elif(request.method == 'GET'):
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

