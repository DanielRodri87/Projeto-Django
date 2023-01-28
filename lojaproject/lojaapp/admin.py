from django.contrib import admin
from.models import *
from django.contrib import admin

admin.site.register([Cliente, Categoria, Produto, Carro, CarroProduto, Pedido_order])
