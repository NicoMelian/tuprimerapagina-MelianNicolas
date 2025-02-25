from django.urls import path
from . import views
from blog import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('crear/', views.crear_articulo, name='crear_articulo'),
    path('comentario/<int:articulo_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('detalle/<int:articulo_id>/', views.detalle_articulo, name='detalle_articulo'),
]
