from django.test import TestCase

from .models import Post

from http import HTTPStatus

# Create your tests here.

""" class PostModelTest(TestCase):
    
    def test_post_model_exist(self):
        posts = Post.objejcts.all()

        self.assertEqual(posts,[]) """


class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = Post.objects.create(
            title="title Post",
            body="Test Body",
        )
        self.assertEqual(str(post), post.title)

        ## os outros dois itens não precisa ser declarado
        # pois pegaram a data de agora


## home page


class HomepageTest(TestCase):
    def setUp(self) -> None:
        post1 = Post.objects.create(
            title="teste post 1", body="Este é um teste para o post 1"
        )

        post2 = Post.objects.create(
            title="Teste de post 2", body="Teste de post para post 2"
        )

    def test_homepage_return_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, "teste post 1")
        self.assertContains(response, "Teste de post 2")


## aula 4

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