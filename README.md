# meu-projeto-django

Meu primeiro projeto django na fabrica!

<p>Caso você esteja com dificuldade em entender o Django acesse este link(<a href="https://drive.google.com/file/d/15LDO6V0MvawO9AjjOWt1k2o8yucbXE3W/view?usp=sharing" target="_blank">Aula Introdução ao DJnago</a>).</p>

```shell
    # Criando venv
    python -m venv venv

    # Crie um .gitignore e escreva /venv/ dentro

    # Ativar venv(Windows)
    .\venv\Scripts\activate

    # Ativar venv(linux e mac)
    source venv/bin/activate

    # Instalar Django
    pip install django

    # Criar requirements.txt
    pip freeze > requirements.txt

    # Criando porjeto django
    django-admin startproject my-app .

    # Criar um app
    #OBS: MeuApp é onde você vai colocar o nome de seu app.
    python manage.py startapp MeuApp

    # usando o django-admin
    django-admin startapp MeuApp

    # Importar seu app no arquivo settings.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            "MeuApp",
        ]

    # Gerando as migrations
    python manage.py makemigrations

    # Executando as migrations
    python manage.py migrate

    # Executando o servidor
    python manage.py runserver

    # Criar super usuário
    python manage.py createsuperuser

```
