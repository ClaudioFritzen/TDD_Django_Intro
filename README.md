Crie o ambiente virtual e ative 
py -m venv venv
venv/Scripts/Activate

Crie um projeto django
django-admin startproject myblog .

rode as migrate
py manage.py migrate

Crie um super usuario
py manage.py createsuperuser


# Rode o servidor
py manage.py runserver

# crie um app django
py manage.py startapp posts

# coloque ele no setting.py


##### Teste 

Criaremos um test para testar as models do app .
Em test.py criaremos nosso primeiro teste para ver se a algo nesse banco.

class PostModelTest(TestCase):
    
    def test_post_model_exist(self):
        posts = Post.objejcts.all()

        self.assertEqual(posts,[])

## esse teste trara todos tudo o que tiver no banco

rode o test

py manage.py test

### resultado 
OK
(venv) PS C:\Users\Bruna Cirigaita\OneDrive\Área de Trabalho\Django Projetos\tddDJANGO> py manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
E
======================================================================
ERROR: test_post_model_exist (posts.tests.PostModelTest.test_post_model_exist)        
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Bruna Cirigaita\OneDrive\Área de Trabalho\Django Projetos\tddDJANGO\posts\tests.py", line 8, in test_post_model_exist
    posts = Post.objejcts.all()
            ^^^^
NameError: name 'Post' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (errors=1)
Destroying test database for alias 'default'...


## Resultado erro esperado, pois não temos um banco feito,

promixo passo criar um banco de dados em models.py

class Post(models.Model):
    title: models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

faça as migrações

py manage.py makemigrations
py maage.py runserver

# Agora import a classe do banco para os testes

from models import NomedoBancoCriado

from .models import Post


rode o test

# Atenção dará erro novamente pois o nosso banco esta vazio,
# sem nenhum dado criado.

# Altere o test para fazer a contagem dos dados do banco
class PostModelTest(TestCase):
    
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts,0)

## rode  o teste e ele funciona

py manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
Destroying test database for alias 'default'...


### Aula 2  sobre teste

# Iremos criar dados fakes para o nosso banco de dados

# isso abaixo do outro test
def test_string_rep_of_objects(self):
        
        post = Post.objects.create(
            title="title Post",
            body='Test Body'
            ## os outros dois itens não precisa ser declarado
            # pois pegaram a data de agora
        )




## testando a homeview

from http import HTTPStatus

class HomepageTest(TestCase):
    
    def setUp(self) -> None:
        Post.objects.create(
            title="teste post 1",
            body='Este é um teste para o post 1'
        )

        Post.objects.create(
            title='Teste de post 2',
            body='Teste de post para post 2'
        )

    def test_homepage_return_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

## criado o test, erro esperado. 

AssertionError: No templates used to render the response

## Agora iremos criar esse html

## mudaremos em settings.py
"DIRS": [BASE_DIR / 'templates'],

e criaremos a seguinte pasta no root do projeto

templates/posts/index.html

# agora vamos pra views.py de posts
 Crie a função
    def index(request):
    return render(request, "posts/index.html")
# Crie a urls.py
    Crie a rota para home views

        from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='homepage'),
]


# na pasta princal redirecione para posts.urls
    path('', include('posts.urls')),


## Rode os teste e é pra funcionar

py manage.py test



## aula 4 

# Criando nosso teste para 
class DetailPageTest(TestCase):
    
    def setUp(self) -> None:
        self.post = Post.objects.create(
        title = 'Couse of js',
        body='Curso para iniciante em JS'
        )

    def test_detail_page_return_correct_response(self):

        response = self.client.get(f'post/{self.id}')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/datail.html')

Iremos criar um teste para ver se está apresentando os detalhes do nosso post, para isso. O nossa resposta esperada será um erro 404.

# Agora criaremos a views de detail passando id 
    Por que faremos isso, quando queremos saber mais detalhes sobre um post temos que pegar o numero da pk (chave primaria) definida quando criamos o post. Para mais informações abra o banco de dados, e olhe o numero do id que será unico no banco.

# Crie a rota para redirecionamento do produto desejado.
    path('post/<int:id>/', views.post_detail, name='post_detail'),


# notasse se rodarmos o test ainda aparecerar o mesmo erro de 404

# crieremos o template html para renderizar o html
    mesmo criando o template html o erro persiste.

# trabalharemos na models
    abaixo de função. criemos outra

     def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.pk})

# agora voltamos no teste e removemos f'string' e deixaremos a rota dinaminca com get.absolute()

class DetailPageTest(TestCase):
    
    def setUp(self) -> None:
        self.post = Post.objects.create(
        title = 'Couse of js',
        body='Curso para iniciante em JS'
        )

    def test_detail_page_return_correct_response(self):

## alteração foi nesta linha
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'posts/detail.html')
    

