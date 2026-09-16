from django import forms
from .models import Acervo


class AcervoForm(forms.ModelForm):
    """
    Formulário para criar e editar acervos
    """

    class Meta:
        model = Acervo
        fields = [
            'titulo',
            'autor',
            'ano',
            'tipo_acervo',
            'categoria',
            'isbn',
            'editora',
            'descricao',
            'disponivel'
        ]

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do acervo'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do autor'
            }),
            'ano': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': '1000',
                'max': '2100'
            }),
            'tipo_acervo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ISBN (opcional)'
            }),
            'editora': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Editora (opcional)'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição ou resumo'
            }),
            'disponivel': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        labels = {
            'titulo': 'Título do Acervo',
            'autor': 'Autor',
            'ano': 'Ano de Publicação',
            'tipo_acervo': 'Tipo de Acervo',
            'categoria': 'Categoria (DDC)',
            'isbn': 'ISBN',
            'editora': 'Editora',
            'descricao': 'Descrição',
            'disponivel': 'Disponível para empréstimo?'
        }


class AcervoSearchForm(forms.Form):
    """
    Formulário para pesquisar acervos
    """

    nome = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Pesquisar por título ou autor'
        }),
        label='Nome/Título'
    )

    tipo_acervo = forms.ChoiceField(
        required=False,
        choices=[('', 'Todos os tipos')] + list(Acervo.TIPO_ACERVO_CHOICES),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Tipo de Acervo'
    )

    categoria = forms.ChoiceField(
        required=False,
        choices=[('', 'Todas as categorias')] + list(Acervo.CATEGORIA_CHOICES),
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label='Categoria (DDC)'
    )
