# Sistema de Biblioteca (Django)

Sistema de gerenciamento de acervo de biblioteca — Aulas 04 e 05.

## Funcionalidades

- CRUD completo de Acervos (criar, listar, editar, deletar)
- Tipo de acervo: Digital ou Físico
- Categoria por Classificação Decimal de Dewey (CDD/DDC) — 10 categorias (000 a 900)
- Pesquisa por nome/título, tipo de acervo e categoria
- Dashboard com estatísticas
- Django Admin customizado

## Como rodar (Windows / PowerShell)

```powershell
# 1. Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar variáveis de ambiente
copy .env.example .env
# edite o .env com os dados do seu PostgreSQL

# 4. Criar as tabelas
python manage.py makemigrations
python manage.py migrate

# 5. Criar um superusuário para acessar o admin
python manage.py createsuperuser

# 6. Rodar o servidor
python manage.py runserver
```

Acesse:
- Site: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin


