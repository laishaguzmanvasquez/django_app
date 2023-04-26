from django.urls import path
from .views import index, categoria, post_detail

# appname = 'aplicaciones.blog'

urlpatterns = [
    path('',index, name='index'),
    path('categoria/<int:cat_id>', categoria, name='categoria'),
    path('post_detail/<slug:slug>', post_detail, name='post_detail'),
]