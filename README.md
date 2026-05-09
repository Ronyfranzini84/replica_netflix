# Hashflix

Projeto web em Django que replica a experiencia de uma plataforma de streaming no estilo Netflix, com foco em autenticacao, catalogo de filmes, detalhes com episodios, historico de visualizacao e pesquisa.

## Visao Geral

O sistema possui uma landing page, fluxo de login/criacao de conta e uma area protegida para usuarios autenticados, onde e possivel:

- Ver filme em destaque.
- Navegar por secoes de filmes recentes e em alta.
- Continuar assistindo com base no historico do usuario.
- Visualizar detalhes de um filme, episodios e relacionados por categoria.
- Pesquisar filmes por titulo.
- Editar dados do perfil e alterar senha.

## Stack Tecnologica

- Python 3
- Django 5.2.13
- SQLite (banco padrao)
- django-crispy-forms + crispy-bootstrap5
- Pillow (upload/manipulacao de imagens)
- Tailwind CSS via CDN e Bootstrap 5 via CDN

Dependencias listadas em [requirements.txt](requirements.txt).

## Estrutura do Projeto

Principais diretorios e arquivos:

- [hashflix/settings.py](hashflix/settings.py): configuracoes do projeto Django.
- [hashflix/urls.py](hashflix/urls.py): roteamento principal.
- [filme/models.py](filme/models.py): modelos Filme, Episodio e Usuario customizado.
- [filme/views.py](filme/views.py): views de homepage, home de filmes, detalhes, pesquisa, perfil e criacao de conta.
- [filme/urls.py](filme/urls.py): rotas da app filme.
- [filme/forms.py](filme/forms.py): formularios de homepage e criacao de conta.
- [filme/novos_context.py](filme/novos_context.py): context processors de filmes recentes e em alta.
- [filme/templates](filme/templates): paginas da aplicacao.
- [templates/base.html](templates/base.html): layout base e navbar global.
- [static](static): css, imagens e scripts.
- [media](media): arquivos enviados pelos modelos (thumbs).

## Modelagem

### Filme

- titulo
- thumb (ImageField)
- descricao
- categoria (ANALISE, PROGRAMACAO, APRESENTACAO, OUTROS)
- visualizacoes
- data_criacao

### Episodio

- relacao com Filme (ForeignKey)
- titulo
- video (URL)

### Usuario (customizado)

- herda de AbstractUser
- filmes_vistos (ManyToMany com Filme)

Configuracao do usuario customizado em [hashflix/settings.py](hashflix/settings.py#L83): AUTH_USER_MODEL = filme.Usuario.

## Funcionalidades Mapeadas

### Publicas

- Landing page ([filme/templates/homepage.html](filme/templates/homepage.html)).
- Redirecionamento inteligente por email na homepage:
	- email existente: vai para login
	- email novo: vai para criar conta

### Autenticacao e Conta

- Login: [filme/urls.py](filme/urls.py#L13)
- Logout: [filme/urls.py](filme/urls.py#L14)
- Criar conta: [filme/urls.py](filme/urls.py#L16)
- Editar perfil: [filme/urls.py](filme/urls.py#L15)
- Mudar senha: [filme/urls.py](filme/urls.py#L17)

### Area Logada

- Home de filmes com destaque e secoes dinamicas ([filme/templates/homefilmes.html](filme/templates/homefilmes.html)).
- Detalhes do filme com:
	- incremento de visualizacoes
	- registro em filmes vistos do usuario
	- listagem de episodios
	- recomendacoes por categoria
- Pesquisa por titulo com icontains.

## Rotas Principais

- / -> homepage
- /filmes/ -> homefilmes
- /filmes/<id>/ -> detalhes do filme
- /pesquisa/?query=texto -> busca
- /login/ -> login
- /logout/ -> logout
- /criarconta/ -> criar conta
- /editarperfil/<id> -> editar perfil
- /mudarsenha/ -> alterar senha

Definidas em [filme/urls.py](filme/urls.py).

## Como Rodar Localmente

### 1. Clonar o repositorio

```bash
git clone https://github.com/Ronyfranzini84/replica_netflix.git
cd replica_netflix
```

### 2. Criar e ativar ambiente virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migracoes

```bash
python manage.py migrate
```

### 5. Criar superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Rodar servidor

```bash
python manage.py runserver
```

Acesse:

- Aplicacao: http://127.0.0.1:8000/
- Admin Django: http://127.0.0.1:8000/admin/

## Midia e Arquivos Estaticos

- STATIC_URL: static/
- STATICFILES_DIRS: pasta [static](static)
- MEDIA_URL: media/
- MEDIA_ROOT: pasta [media](media)

Em desenvolvimento, as configuracoes de [hashflix/urls.py](hashflix/urls.py) ja servem arquivos estaticos e de media.

## Painel Admin

No admin, os modelos Filme, Episodio e Usuario estao registrados em [filme/admin.py](filme/admin.py).

O Usuario utiliza UserAdmin customizado com campo adicional de historico (filmes_vistos).

## Estado Atual do Projeto

- Projeto funcional para fluxo principal de streaming educacional.
- Banco local SQLite configurado.
- Testes automatizados ainda nao implementados ([filme/tests.py](filme/tests.py)).
- README anterior estava vazio; este documento foi criado a partir da analise do codigo.

## Sugestoes de Evolucao

- Adicionar suite de testes (models, views e autenticacao).
- Implementar paginacao na busca e nas secoes da home.
- Melhorar seguranca para ambiente de producao (DEBUG, ALLOWED_HOSTS, segredo por variavel de ambiente).
- Criar seeds/fixtures para popular filmes e episodios facilmente.
- Separar melhor estilos customizados para arquivos CSS dedicados.

## Licenca

Este projeto nao possui licenca declarada ate o momento.
