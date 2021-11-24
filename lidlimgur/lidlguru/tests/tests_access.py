from django.test import Client, TestCase
from lidlguru.models import Answer, Comment, Post
from lidlguru.tests.factories.factories import (AnswerFactory, CommentFactory,
                                                CustomUserFactory, PostFactory)


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
        response = self.c.get('/answer/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_answer_as_not_logged_user(self):
        comment_dummy = CommentFactory()
        response = self.c.get('/comment/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_post_as_logged_user(self):
        self.c.force_login(self.user, backend=None)
        post_dummy = PostFactory()
        response = self.c.get('/post/')
        self.assertEqual(response.status_code, 200)

    def test_access_to_answer_as_logged_user(self):
        self.c.force_login(self.user, backend=None)
        answer_dummy = AnswerFactory()
        response = self.c.get('/answer/')
        self.assertEqual(response.status_code, 200)

    def test_access_to_comment_as_logged_user(self):
        self.c.force_login(self.user, backend=None)
        comment_dummy = CommentFactory()
        response = self.c.get('/comment/')
        self.assertEqual(response.status_code, 200)

    def test_access_to_user_as_not_logged_user(self):
        custom_user_dummy = CustomUserFactory()
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_user_as_logged_user(self):
        custom_user_dummy = CustomUserFactory()
        self.c.force_login(self.user, backend=None)
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, 403)

    def test_access_to_user_as_admin(self):
        custom_user_dummy = CustomUserFactory(is_superuser=True, is_staff=True)
        self.c.force_login(custom_user_dummy, backend=None)
        response = self.c.get('/user/')
        self.assertEqual(response.status_code, 200)
