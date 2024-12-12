from django.urls import path
from . import views
from .views import (
    LivroListView, LivroCreateView, LivroUpdateView, LivroDeleteView,
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    EditoraListView, EditoraCreateView, EditoraUpdateView, EditoraDeleteView,
    UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView,
    EmprestimoListView, EmprestimoCreateView, EmprestimoUpdateView, EmprestimoDeleteView,
    AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView 
)
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.base, name='base'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('autores/', AutorListView.as_view(), name='listar_autores'),
    path('autores/criar/', AutorCreateView.as_view(), name='criar_autor'),
    path('autores/editar/<int:id>/', AutorUpdateView.as_view(), name='editar_autor'),
    path('autores/deletar/<int:id>/', AutorDeleteView.as_view(), name='deletar_autor'),

    path('livros/', LivroListView.as_view(), name='listar_livros'),
    path('livros/criar/', LivroCreateView.as_view(), name='criar_livro'),
    path('livros/editar/<int:pk>/', LivroUpdateView.as_view(), name='editar_livro'),
    path('livros/deletar/<int:pk>/', LivroDeleteView.as_view(), name='deletar_livro'),

    path('categorias/', CategoriaListView.as_view(), name='listar_categorias'),
    path('categorias/criar/', CategoriaCreateView.as_view(), name='criar_categoria'),
    path('categorias/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/deletar/<int:pk>/', CategoriaDeleteView.as_view(), name='deletar_categoria'),

    path('editoras/', EditoraListView.as_view(), name='listar_editoras'),
    path('editoras/criar/', EditoraCreateView.as_view(), name='criar_editora'),
    path('editoras/editar/<int:pk>/', EditoraUpdateView.as_view(), name='editar_editora'),
    path('editoras/deletar/<int:pk>/', EditoraDeleteView.as_view(), name='deletar_editora'),

    path('usuarios/', UsuarioListView.as_view(), name='listar_usuarios'),
    path('usuarios/criar/', UsuarioCreateView.as_view(), name='criar_usuario'),
    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar_usuario'),
    path('usuarios/deletar/<int:pk>/', UsuarioDeleteView.as_view(), name='deletar_usuario'),

    path('emprestimos/', EmprestimoListView.as_view(), name='listar_emprestimos'),
    path('emprestimos/criar/', EmprestimoCreateView.as_view(), name='criar_emprestimo'),
    path('emprestimos/editar/<int:pk>/', EmprestimoUpdateView.as_view(), name='editar_emprestimo'),
    path('emprestimos/deletar/<int:pk>/', EmprestimoDeleteView.as_view(), name='deletar_emprestimo'),
]
