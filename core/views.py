from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import path
from .models import Livro, Autor, Categoria, Editora, Usuario, Emprestimo
from .forms import LivroForm, AutorForm, CategoriaForm, EditoraForm, UsuarioForm, EmprestimoForm
from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

class LivroListView(ListView):
    model = Livro
    template_name = 'livros/listar.html'
    context_object_name = 'livros'

class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livros/criar.html'
    success_url = reverse_lazy('listar_livros')

class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'livros/editar.html'
    success_url = reverse_lazy('listar_livros')

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'livros/deletar.html'
    success_url = reverse_lazy('listar_livros')

class AutorListView(ListView):
    model = Autor
    template_name = 'autores/listar.html'
    context_object_name = 'autores'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/criar.html'
    success_url = reverse_lazy('listar_autores')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autores/editar.html'
    success_url = reverse_lazy('listar_autores')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autores/deletar.html'
    success_url = reverse_lazy('listar_autores')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/listar.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/criar.html'
    success_url = reverse_lazy('listar_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/editar.html'
    success_url = reverse_lazy('listar_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/deletar.html'
    success_url = reverse_lazy('listar_categorias')

class EditoraListView(ListView):
    model = Editora
    template_name = 'editoras/listar.html'
    context_object_name = 'editoras'

class EditoraCreateView(CreateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'editoras/criar.html'
    success_url = reverse_lazy('listar_editoras')

class EditoraUpdateView(UpdateView):
    model = Editora
    form_class = EditoraForm
    template_name = 'editoras/editar.html'
    success_url = reverse_lazy('listar_editoras')

class EditoraDeleteView(DeleteView):
    model = Editora
    template_name = 'editoras/deletar.html'
    success_url = reverse_lazy('listar_editoras')

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/listar.html'
    context_object_name = 'usuarios'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/criar.html'
    success_url = reverse_lazy('listar_usuarios')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/editar.html'
    success_url = reverse_lazy('listar_usuarios')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/deletar.html'
    success_url = reverse_lazy('listar_usuarios')

class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = 'emprestimos/listar.html'
    context_object_name = 'emprestimos'

class EmprestimoCreateView(CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimos/criar.html'
    success_url = reverse_lazy('listar_emprestimos')

class EmprestimoUpdateView(UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimos/editar.html'
    success_url = reverse_lazy('listar_emprestimos')

class EmprestimoDeleteView(DeleteView):
    model = Emprestimo
    template_name = 'emprestimos/deletar.html'
    success_url = reverse_lazy('listar_emprestimos')
