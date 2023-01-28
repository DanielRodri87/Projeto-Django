from django.shortcuts import render
from django.views.generic import TemplateView
from.models import *

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_list'] = Produto.objects.all().order_by('-id')
        return context
    
class TodosProdutosView(TemplateView):
    template_name = "todosprodutos.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todoscategorias'] = Categoria.objects.all()
        return context

class ProdutoDetalheView(TemplateView):
    template_name = "produtodetalhe.html"
    
class SobreView(TemplateView):
    template_name = "sobre.html"
    
class ContatoView(TemplateView):
    template_name = "contato.html"
    
