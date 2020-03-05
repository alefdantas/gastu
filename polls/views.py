from django.shortcuts import render, get_object_or_404,HttpResponseRedirect, redirect
from .forms import FormCardapio, mapForm, FormRestaurante
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
#def exibirCardapio(request):
    #exibir = Prato.objects.all().order_by('-created_at')
    #return render(request,'exibirCardapio.html', {'pratos': Prato.objects.all()})
def exibirRestaurante(request):
    exibir = Restaurante.objects.all().order_by('-created_at')
    return render(request,'exibirRestaurante.html', {'restaurantes': Restaurante.objects.all()})
def cadastro_de_cardapio(request):
    form = FormCardapio()
    user = request.user
    if request.method == 'POST':
        form = FormCardapio(request.POST, request.FILES)
        print(form.errors );
        if form.is_valid():
            post_restaurante = form.cleaned_data['restaurante']
            post_foto = form.cleaned_data['foto']
            post_nome = form.cleaned_data['nome']
            post_descricao = form.cleaned_data['descricao']
            post_valor = form.cleaned_data['valor']
            post_disponibilidade = form.cleaned_data['disponibilidade']
            new_post = Prato(restaurante=post_restaurante,foto=post_foto, nome=post_nome, descricao=post_descricao, valor=post_valor, disponibilidade=post_disponibilidade)
            new_post.save()
            return redirect('gastu:post_list')
    elif(request.method == 'GET'):
        return render(request, 'cadastrarCardapio.html', {'form': form})
def cadastro_de_restaurante(request):
    form = FormRestaurante()
    user = request.user
    if request.method == 'POST':
        form = FormRestaurante(request.POST, request.FILES)
        print(form.errors );
        if form.is_valid():
            post_cnpj = form.cleaned_data['cnpj']
            post_nome = form.cleaned_data['nome']
            post_nome_comercial = form.cleaned_data['nome_comercial']
            post_descricao = form.cleaned_data['descricao']
            post_imagem = form.cleaned_data['imagem']
            post_latitude = form.cleaned_data['latitude']
            post_longitude = form.cleaned_data['longitude']
            new_post = Restaurante(cnpj=post_cnpj, nome=post_nome,nome_comercial=post_nome_comercial, descricao=post_descricao, imagem=post_imagem, latitude=post_latitude, longitude=post_longitude)
            new_post.save()
            return redirect('polls:cadastro_de_cardapio')
    elif(request.method == 'GET'):
        return render(request, 'cadastrarRestaurante.html', {'form': form})
def deletar_restaurante(request):
    this_object_id = request.GET['id_delet']
    post = Restaurante.objects.get(id_restaurante=this_object_id)
    form = FormRestaurante(instance=post)
    if request.method == 'GET':
        consulta = Restaurante.objects.get(id_restaurante=this_object_id)
        consulta.delete()    
    return redirect('gastu:post_list')
    
def deletar_cardapio(request):
    this_object_id = request.GET['id_delet']
    post = Prato.objects.get(id_prato=this_object_id)
    form = FormCardapio(instance=post)
    if request.method == 'GET':
        consulta = Prato.objects.get(id_prato=this_object_id)
        consulta.delete()    
    return redirect('gastu:post_list')
    

def mapView(request):
    exibir = Restaurante.objects.all()
    return render(request, "cadastrarRestaurante.html" ,{"form":Restaurante.objects.all()})

def update_cardapio(request):
    this_object_id = request.GET.get("id_upd")
    post = Prato.objects.get(id_prato=this_object_id)
    form = FormCardapio(instance=post)
    user = request.user
    if request.method == 'POST':
        form = FormCardapio(request.POST,instance=post)
        if form.is_valid():
            post_restaurante = form.cleaned_data['restaurante']
            post_foto = form.cleaned_data['foto']
            post_nome = form.cleaned_data['nome']
            post_descricao = form.cleaned_data['descricao']
            post_valor = form.cleaned_data['valor']
            post_disponibilidade = form.cleaned_data['disponibilidade']
            new_post = Prato(restaurante=post_restaurante,foto=post_foto, nome=post_nome, descricao=post_descricao, valor=post_valor, disponibilidade=post_disponibilidade)
            new_post.save()
        return redirect('gastu:post_list')
    elif(request.method == 'GET'):
        return render(request, 'editarCardapio.html', {'form': form, 'post': post})
def update_restaurante(request):
    this_object_id = request.GET['id_res']
    post = Restaurante.objects.get(id_restaurante=this_object_id)
    form = FormRestaurante(instance=post)
    if request.method == 'POST':
        form = FormRestaurante(request.POST, instance=post)
        print(form.errors );
        if form.is_valid():
            post_cnpj = form.cleaned_data['cnpj']
            post_nome = form.cleaned_data['nome']
            post_nome_comercial = form.cleaned_data['nome_comercial']
            post_descricao = form.cleaned_data['descricao']
            post_imagem = form.cleaned_data['imagem']
            new_post = Restaurante(cnpj=post_cnpj, nome=post_nome,nome_comercial=post_nome_comercial, descricao=post_descricao,imagem=post_imagem)
            new_post.save()
            return redirect('gastu:post_list')
    elif(request.method == 'GET'):
        return render(request, 'editarRestaurante.html', {'form': form, 'post': post})
def adminRestaurante(request):
    return render(request,'adminRestaurante.html', {'restaurantes' : Restaurante.objects.all(),})

def exibeCarda(request):
    this_object_id = request.GET['id_res']
    r = Restaurante.objects.get(id_restaurante=this_object_id)
    pratos = Prato.objects.filter(restaurante=r)
    print(len(pratos))
    return render(request, 'exibirCardapio.html', {'prts':pratos})