<h1>Django Scrapy Prices ESPN</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=python&message=3.9.0&color=3776AB&style=for-the-badge&logo=PYTHON"/>
  <img src="https://img.shields.io/static/v1?label=Heroku&message=deploy&color=430098&style=for-the-badge&logo=heroku"/>
  <img src="http://img.shields.io/static/v1?label=Django&message=x.x.x&color=092E20&style=for-the-badge&logo=Django"/>
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=green&style=for-the-badge"/>
</p>

### :checkered_flag: Tópicos 

:pushpin: [Descrição do projeto](#descrição-do-projeto)

:pushpin: [Funcionalidades](#funcionalidades)

:pushpin: [Deploy da Aplicação](#deploy-da-aplicação)

:pushpin: [Pré-requisitos](#pré-requisitos)

:pushpin: [Como rodar a aplicação](#como-rodar-a-aplicação)

## Descrição do Projeto
<p align="justify">
  
  **Houve uma atualização das páginas e o scrapy não está mais funcionando.**
   
  Faz o scrapy dos preços de alguns jogos da PSN.
   
  The Witcher 3 - AC Valhalla - Greedfall - UntilDawn - Immortals Fenyx Rising - God of War
   
   Desenvolvi esse para analisar e comparar os preços dos jogos que tenho interesse em uma única página.
</p>

## Funcionalidades
:white_check_mark: Scrapy preços de alguns jogos da PSN.

## Deploy Aplicação
* [Heroku](https://django-psn-scrapy-im.herokuapp.com/)

## Pré Requisitos
* Python 3.x
* Django 3.1.x
* beautifulsoup4==4.9.3
* urllib3==1.26.2

## Como rodar a aplicação
    1. Clone o projeto

    git clone https://github.com/Italo11Marcos/scrapy-prices-psn.git

    2. Crie um virtualenv
    
    virtualenv venv --python=3.x.x

    3. Ative o seu virtualenv. 

    source venv/bin/activate

    4. Instale dependências

    pip3 -r install requirements.txt

    5. Execute o projeto

    python3 manage.py runserver

## Considerações

Bibliotecas utilizas:
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [urllib3](https://pypi.org/project/urllib3/)






