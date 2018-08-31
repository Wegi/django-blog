from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blogengine.models import Post

class PostTest(TestCase):
    def test_create_post(self):
        post = Post()
        post.title = "Test post"
        post.text = "Hello World!"
        post.pub_date = timezone.now()
        post.save()

        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts.first()
        self.assertEquals(only_post, post)

        self.assertEquals(only_post.title, "Test post")
        self.assertEquals(only_post.text, "Hello World!")