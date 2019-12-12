from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def post_list(request):
	posts = Post.objects.all().order_by('-created_at')
	return render(request, 'gastu/post_list.html', {'posts':posts})

def about(request):
	return render(request, 'gastu/about_us.html')

def contact(request):
	return render(request, 'gastu/contact.html')

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'gastu/post_detail.html', {'post':post})

def tourism(request):
	return render(request, 'gastu/tourism.html')

def gastronomy(request):
	return render(request, 'gastu/gastronomy.html')

def rn(request):
	return render(request, 'gastu/rn.html')

def idea(request):
	return render(request, 'gastu/idea.html')

def detail(request):
	return render(request, 'gastu/detail.html')

