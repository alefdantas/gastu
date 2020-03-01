from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from polls.models import Restaurante, Prato

def exibeRestaurantes(request):
    return render(request,'gastu/base2.html', {'restaurantes' : Restaurante.objects.all()})

def post_list(request):
	restaurantes = Restaurante.objects.all()
	return render(request, 'gastu/post_list.html', {'lista_de_restaurantes':restaurantes})

def about(request):
	return render(request, 'gastu/about_us.html')

def contact(request):
	return render(request, 'gastu/contact.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'gastu/post_detail.html', {'post':post})

def detail(request):
    # this_object_id = 1
    this_object_id = request.GET['id_res']
    r = Restaurante.objects.get(id_restaurante=this_object_id)
    pratos = Prato.objects.filter(restaurante=r)
    print(len(pratos))
    return render(request, 'gastu/detail.html', {'prs':pratos})

