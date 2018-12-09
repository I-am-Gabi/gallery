# Gallery

Sistema para fazer upload de fotos para a aws s3 e visualizar as fotos aprovadas.

### Requirements

* Django~=2.0.6
* gunicorn==19.6.0
* psycopg2-binary
* dj-database-url==0.5.0
* whitenoise==3.3.0
* django_heroku
* boto3 

Para instalar os pacotes exigidos:

```
pip install -r requirements.txt  
```


### Instruções para rodar o projeto

Clone o repositório:

```
git clone https://github.com/I-am-Gabi/gallery.git
```

Crie o banco de dados:

```
python manage.py migrate
python manage.py makemigrations photo_gallery
python manage.py migrate photo_gallery

```

Crie um super usuário:

```
python manage.py createsuperuser
```

Configure as variáveis de ambiente para a aplicação se comunicar com o bucket criado na aws.

```
AWS_ACCESS_KEY_ID='<key_id>'
AWS_SECRET_ACCESS_KEY='<secret>'
```

Rode o servidor:

```
python manage.py runserver

```

No browser acesse:

```
http://localhost:8000/

```

### Navegue pelo projeto

A [tela inicial](http://localhost:8000/) apresenta as fotos da galeria, após serem aprovadas. 
Você pode fazer o upload de novas fotos clicando no menu [Upload](http://127.0.0.1:8000/gallery/upload_photo).
Se você voltar para a galeria verá que as fotos upadas não aparecem na tela, isso acontece porque você precisa aprová-las primeiro.

Acesse a página para de [aprovação](http://127.0.0.1:8000/gallery/approve). Você terá que logar com o super usuário que criou no início da configuração do projeto. Após o login, você verá as fotos upadas, e se elas foram aprovadas ou não. É possível ainda aprovar uma foto que antes foi desaprovado, assim como desaprovar fotos antes aprovadas. Depois da aprovação acesse a [tela inicial](http://localhost:8000/) e veja o resultado.


### references

1. template base para o projeto https://github.com/ashleydw/lightbox