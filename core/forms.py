from django import forms
from .models import Livro, Autor, Categoria, Editora, Usuario, Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'editora', 'usuario', 'categoria']
        widgets = {
            'autores': forms.CheckboxSelectMultiple,
            'usuario': forms.CheckboxSelectMultiple,
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'data_nascimento']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'cidade']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro', 'data_emprestimo', 'data_devolucao']
        widgets = {
            'data_emprestimo': forms.SelectDateWidget(years=range(2000, 2025)),
            'data_devolucao': forms.SelectDateWidget(years=range(2000, 2025)),
        }
