import factory
from django.test import TestCase
from django.test import Client
from django.db.models import signals

from lidlguru.models import Post, Answer, Comment
from lidlguru.tests.factories.factories import CustomUserFactory, PostFactory, AnswerFactory, \
    CommentFactory


class TestAccess(TestCase):
    @classmethod
    def setUpClass(self):
        self.c = Client()
        self.user = CustomUserFactory(username='UserName')

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        Post.objects.filter().delete()
        Answer.objects.filter().delete()
        Comment.objects.filter().delete()

    def test_access_to_post_as_not_logged_user(self):
        post_dummy = PostFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_comment_as_not_logged_user(self):
        answer_dummy = AnswerFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_answer_as_not_logged_user(self):
        comment_dummy = CommentFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_post_as_looged_user(self):
        self.c.force_login(self.user, backend=None)
        post_dummy = PostFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 200)

    def test_access_to_answer_as_looged_user(self):
        self.c.force_login(self.user, backend=None)
        answer_dummy = AnswerFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 200)

    def test_access_to_comment_as_looged_user(self):
        self.c.force_login(self.user, backend=None)
        comment_dummy = CommentFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 200)

