from django import forms
from .models import Articulo, Comentario

# Formulario para el modelo Articulo
class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'autor', 'contenido', 'categoria']
        widgets = {'categoria': forms.Select()}
              # Asegura que se use un select para las categorías }

# Formulario para el modelo Comentario
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
