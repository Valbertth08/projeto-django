from django.urls import path
from galeria.views import index,imagem #importei as funções da galeria
#representa os caminhos para as views desse componente(endpoint)
urlpatterns=[
    path('', index, name='index'),
    path('imagem/',imagem, name='imagem')# indico que eu quero abri esse caminho
]