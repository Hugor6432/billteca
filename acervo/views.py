from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Acervo
from .forms import AcervoForm, AcervoSearchForm


def lista_acervos(request):
    """
    Lista todos os acervos com opção de pesquisa
    """
    acervos = Acervo.objects.all()
    form_search = AcervoSearchForm(request.GET or None)

    if form_search.is_valid():
        nome = form_search.cleaned_data.get('nome')
        tipo_acervo = form_search.cleaned_data.get('tipo_acervo')
        categoria = form_search.cleaned_data.get('categoria')

        if nome:
            acervos = acervos.filter(
                Q(titulo__icontains=nome) | Q(autor__icontains=nome)
            )

        if tipo_acervo:
            acervos = acervos.filter(tipo_acervo=tipo_acervo)

        if categoria:
            acervos = acervos.filter(categoria=categoria)

    contexto = {
        'acervos': acervos,
        'form_search': form_search,
        'total': acervos.count(),
        'disponivel': acervos.filter(disponivel=True).count(),
        'indisponivel': acervos.filter(disponivel=False).count(),
    }

    return render(request, 'acervo/lista.html', contexto)


def detalhe_acervo(request, pk):
    """
    Exibe os detalhes de um acervo específico
    """
    acervo = get_object_or_404(Acervo, pk=pk)

    contexto = {
        'acervo': acervo,
    }

    return render(request, 'acervo/detalhe.html', contexto)


def criar_acervo(request):
    """
    Cria um novo acervo
    """
    if request.method == 'POST':
        form = AcervoForm(request.POST)
        if form.is_valid():
            acervo = form.save()
            messages.success(request, f'Acervo "{acervo.titulo}" criado com sucesso!')
            return redirect('acervo:lista_acervos')
        else:
            messages.error(request, 'Erro ao criar o acervo. Verifique os campos.')
    else:
        form = AcervoForm()

    contexto = {
        'form': form,
        'titulo': 'Novo Acervo',
        'botao': 'Criar Acervo'
    }

    return render(request, 'acervo/form.html', contexto)


def editar_acervo(request, pk):
    """
    Edita um acervo existente
    """
    acervo = get_object_or_404(Acervo, pk=pk)

    if request.method == 'POST':
        form = AcervoForm(request.POST, instance=acervo)
        if form.is_valid():
            acervo = form.save()
            messages.success(request, f'Acervo "{acervo.titulo}" atualizado com sucesso!')
            return redirect('acervo:detalhe_acervo', pk=acervo.pk)
        else:
            messages.error(request, 'Erro ao atualizar o acervo. Verifique os campos.')
    else:
        form = AcervoForm(instance=acervo)

    contexto = {
        'form': form,
        'acervo': acervo,
        'titulo': 'Editar Acervo',
        'botao': 'Atualizar Acervo'
    }

    return render(request, 'acervo/form.html', contexto)


def deletar_acervo(request, pk):
    """
    Deleta um acervo
    """
    acervo = get_object_or_404(Acervo, pk=pk)

    if request.method == 'POST':
        titulo = acervo.titulo
        acervo.delete()
        messages.success(request, f'Acervo "{titulo}" deletado com sucesso!')
        return redirect('acervo:lista_acervos')

    contexto = {
        'acervo': acervo,
    }

    return render(request, 'acervo/confirmar_delecao.html', contexto)


def dashboard(request):
    """
    Página inicial com estatísticas
    """
    total_acervos = Acervo.objects.count()
    acervos_digitais = Acervo.objects.filter(tipo_acervo='digital').count()
    acervos_fisicos = Acervo.objects.filter(tipo_acervo='fisico').count()
    acervos_disponiveis = Acervo.objects.filter(disponivel=True).count()

    categorias = {}
    for codigo, nome in Acervo.CATEGORIA_CHOICES:
        count = Acervo.objects.filter(categoria=codigo).count()
        categorias[nome] = count

    ultimos_acervos = Acervo.objects.all()[:5]

    contexto = {
        'total_acervos': total_acervos,
        'acervos_digitais': acervos_digitais,
        'acervos_fisicos': acervos_fisicos,
        'acervos_disponiveis': acervos_disponiveis,
        'categorias': categorias,
        'ultimos_acervos': ultimos_acervos,
    }

    return render(request, 'acervo/dashboard.html', contexto)
