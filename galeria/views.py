from django.shortcuts import render

def index(request): #processo a requisição(da url) e devolvo o arquivo necessario
    return render(request,'galeria/index.html')

def imagem(request):
    return render(request,'galeria/imagem.html')
