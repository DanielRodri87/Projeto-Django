from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
    
class SobreView(TemplateView):
    template_name = "sobre.html"
    
class ContatoView(TemplateView):
    template_name = "contato.html"