from django.shortcuts import render
from .forms import SalvarIten
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