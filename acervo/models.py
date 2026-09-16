from django.db import models
from django.core.validators import MinValueValidator


class Acervo(models.Model):
    """
    Modelo para representar um acervo/livro na biblioteca
    """

    TIPO_ACERVO_CHOICES = [
        ('digital', 'Digital'),
        ('fisico', 'Físico'),
    ]

    CATEGORIA_CHOICES = [
        ('000', '000 - Generalidades e Informação'),
        ('100', '100 - Filosofia e Psicologia'),
        ('200', '200 - Religião e Teologia'),
        ('300', '300 - Ciências Sociais e Direito'),
        ('400', '400 - Linguística e Idiomas'),
        ('500', '500 - Ciências Puras (Exatas e Naturais)'),
        ('600', '600 - Ciências Aplicadas (Tecnologia)'),
        ('700', '700 - Artes e Recreação'),
        ('800', '800 - Literatura'),
        ('900', '900 - História e Geografia'),
    ]

    titulo = models.CharField(
        max_length=255,
        verbose_name='Título',
        help_text='Título do acervo'
    )

    autor = models.CharField(
        max_length=150,
        verbose_name='Autor',
        help_text='Nome do autor ou criador'
    )

    ano = models.IntegerField(
        validators=[MinValueValidator(1000)],
        verbose_name='Ano de Publicação',
        help_text='Ano em que foi publicado'
    )

    tipo_acervo = models.CharField(
        max_length=10,
        choices=TIPO_ACERVO_CHOICES,
        default='fisico',
        verbose_name='Tipo de Acervo',
        help_text='Se é digital ou físico'
    )

    categoria = models.CharField(
        max_length=100,
        choices=CATEGORIA_CHOICES,
        verbose_name='Categoria (DDC)',
        help_text='Classificação Decimal de Dewey'
    )

    disponivel = models.BooleanField(
        default=True,
        verbose_name='Disponível',
        help_text='Se o acervo está disponível para empréstimo'
    )

    descricao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição',
        help_text='Descrição ou resumo do acervo'
    )

    isbn = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        verbose_name='ISBN',
        help_text='Código ISBN do livro'
    )

    editora = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Editora',
        help_text='Nome da editora'
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )

    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Acervo'
        verbose_name_plural = 'Acervos'
        indexes = [
            models.Index(fields=['titulo']),
            models.Index(fields=['categoria']),
            models.Index(fields=['tipo_acervo']),
        ]

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"

    def get_tipo_acervo_display_custom(self):
        """Retorna tipo de acervo em português"""
        return dict(self.TIPO_ACERVO_CHOICES).get(self.tipo_acervo)

    def get_categoria_display_custom(self):
        """Retorna categoria completa"""
        return dict(self.CATEGORIA_CHOICES).get(self.categoria)
