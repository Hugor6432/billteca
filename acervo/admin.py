from django.contrib import admin
from .models import Acervo


@admin.register(Acervo)
class AcervoAdmin(admin.ModelAdmin):
    """
    Configuração do painel administrativo para o modelo Acervo
    """

    list_display = (
        'titulo',
        'autor',
        'ano',
        'tipo_acervo',
        'categoria',
        'disponivel',
        'data_criacao'
    )

    list_filter = (
        'tipo_acervo',
        'categoria',
        'disponivel',
        'ano',
        'data_criacao'
    )

    search_fields = (
        'titulo',
        'autor',
        'isbn',
        'editora'
    )

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'autor', 'ano', 'isbn', 'editora')
        }),
        ('Classificação', {
            'fields': ('tipo_acervo', 'categoria')
        }),
        ('Detalhes', {
            'fields': ('descricao', 'disponivel'),
            'classes': ('collapse',)
        }),
        ('Dados do Sistema', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('data_criacao', 'data_atualizacao')

    ordering = ('-data_criacao',)

    def get_queryset(self, request):
        """Otimiza a query do admin"""
        queryset = super().get_queryset(request)
        return queryset.select_related()

    actions = ['marcar_disponivel', 'marcar_indisponivel']

    @admin.action(description='Marcar como disponível')
    def marcar_disponivel(self, request, queryset):
        queryset.update(disponivel=True)

    @admin.action(description='Marcar como indisponível')
    def marcar_indisponivel(self, request, queryset):
        queryset.update(disponivel=False)
