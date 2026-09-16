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

## Publicar no GitHub

```powershell
git init
git add .
git commit -m "COMMIT 1: Inicializar projeto Django e configurar ambiente virtual"
git branch -M main
git remote add origin <URL_DO_SEU_REPOSITORIO>
git push -u origin main
```

O `.env` não é versionado (está no `.gitignore`); use o `.env.example` como referência.

## Colocar o site no ar (deploy no Render)

O projeto já vem pronto para deploy no [Render](https://render.com) (tem plano free, com banco PostgreSQL incluso).

1. Crie uma conta gratuita em https://render.com e conecte sua conta do GitHub.
2. No painel do Render, clique em **New +** → **Blueprint**.
3. Selecione o repositório que você acabou de subir (o Render detecta o arquivo `render.yaml` automaticamente e já configura o serviço web + o banco de dados).
4. Clique em **Apply** — o Render vai instalar as dependências, rodar as migrations e subir o site sozinho.
5. Quando terminar (alguns minutos), o Render te dá um link do tipo `https://biblioteca-django.onrender.com` — é esse link que abre o site já funcionando.
6. Para acessar o `/admin`, crie o superusuário direto pelo terminal (Shell) do serviço no painel do Render:
   ```
   python manage.py createsuperuser
   ```

Observação: no plano free, o Render "dorme" o serviço após um tempo sem acesso — o primeiro acesso depois disso pode demorar uns 30-50 segundos para acordar.
