
from django.contrib import admin
from django.urls import path, include #inclui a url dos aplicativos(componentes)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
