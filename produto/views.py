from django.shortcuts import render,redirect
from .models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    return render(request,'index.html',{'produtos':produtos})

def cad(request):
    return render(request,'cad.html',{})

def salvar(request):
    vdescricao = request.POST['descricao']
    vpreco = request.POST['preco']
    Produto.objects.create(descricao=vdescricao,preco=vpreco)
    produtos = Produto.objects.all()
    return render(request,'index.html',{'produtos':produtos})

def detalhe(request,id):
    produto = Produto.objects.get(id=id)
    return render(request,'detalhe.html',{'produto':produto})

def atu(request,id):
    produto = Produto.objects.get(id=id)
    return render(request,'atu.html',{'produto':produto})

def update(request):
    id = request.POST['id']
    produto = Produto.objects.get(id=id)
    produto.descricao = request.POST['descricao']
    produto.preco = request.POST['preco']
    produto.save()
    return redirect(home)

def delete(request,id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(home)