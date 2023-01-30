from django.shortcuts import render
from django.views.generic import TemplateView
from.models import *
# importar Q
from django.db.models import Q

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        produto = Produto.objects.get(slug=url_slug)
        context['detalhes'] = produto
        return context
    
class AddCarroView(TemplateView):
    template_name = "addcarro.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto_id = self.kwargs['pro_id']
        produto_obj = Produto.objects.get(id=produto_id)
        Carro_id = self.request.session.get('carro_id', None)

        if Carro_id:
            carro_obj = Carro.objects.get(id=Carro_id)
            
        else:
            carro_obj = Carro.objects.create(total=0)
            self.request.session['carro_id'] = carro_obj.id
            
    
class SobreView(TemplateView):
    template_name = "sobre.html"
    
class ContatoView(TemplateView):
    template_name = "contato.html"
    
class SearchView(TemplateView):
    template_name = "search.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        resultado = None
        if query:
            resultado = Produto.objects.filter(
                Q(titulo__icontains=query) | Q(descricao__icontains=query)
            )
        context.update({
            'resultado': resultado
        })
        return context
    
    
