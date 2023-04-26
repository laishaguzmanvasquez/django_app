from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *

# Create your views here.

def index(request):
    """Returns @color_list"""
    post = None
    
    if request.GET.get("q"):

        posts = Post.objects.filter(
            Q(titulo__icontains=request.GET.get("q")) |
            Q(description__icontains=request.GET.get("q"))
        )
    else:
        posts = Post.objects.filter(estado = True)
    
    
    
    context = {'posts': posts, 'cat_menu':get_menu_categorias()}
    return render(request,'index.html',context)

def categoria(request,cat_id:int):
    if cat_id:
        categoria = Categoria.objects.get(pk=cat_id)
        posts = Post.objects.filter(estado = True, categoria = categoria)
        context = {'cat_menu':get_menu_categorias(), 'posts':posts, 'categoria':categoria}
        return  render(request, 'categoria.html', context)

def post_detail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post_detail': post_detail})


def get_menu_categorias():
    menu_cat = Categoria.objects.filter(estado = True)
    return menu_cat.order_by('id')