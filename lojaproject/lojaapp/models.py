from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    titulo = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300, null=True, blank=True)
    endereco = models.CharField(max_length=300, null=True, blank=True)
    data_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome_completo

class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.titulo

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='produtos')
    image2 = models.ImageField(upload_to='produtos', null=True, blank=True)
    image3 = models.ImageField(upload_to='produtos', null=True, blank=True)
    image4 = models.ImageField(upload_to='produtos', null=True, blank=True)
    preco_mercado = models.PositiveIntegerField()
    venda = models.PositiveIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300, null=True, blank=True)
    return_devolucao = models.CharField(max_length=300, null=True, blank=True)
    visualizacao = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titulo

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Carro" + str(self.id)
    
    
    
    

class CarroProduto(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    
    def __str__(self):
        return "Carro:" + str(self.carro.id)+"CarroProduto: " + str(self.id)
    
    
PEDIDO_STATUS= (
    ("Pedido Recebido", "Pedido Recebido"),
    ("Pedido Processando", "Pedido Processando"),
    ("Pedido Caminho", "Pedido Caminho"),
    ("Pedido Completado", "Pedido Completado"),
    ("Pedido Cancelado", "Pedido Cancelado")
)  
    
class Pedido_order(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE)
    ordenando_por = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    disconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    pedido_status = models.PositiveIntegerField(choices=PEDIDO_STATUS)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Pedido_order:" + str(self.id)
    
    
    
