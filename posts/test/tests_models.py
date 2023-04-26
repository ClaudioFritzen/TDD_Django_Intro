from django.test import TestCase


from ..models import Post

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
