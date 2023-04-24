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



