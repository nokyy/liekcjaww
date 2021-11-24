from django.test import TestCase
from lidlguru.models import Answer, Comment, CustomUser, Post
from lidlguru.tests.factories.factories import (AnswerFactory, CommentFactory,
                                                CustomUserFactory, PostFactory)


class TestModels(TestCase):
    def tearDown(self):
        Post.objects.filter().delete()
        Comment.objects.filter().delete()
        Answer.objects.filter().delete()

    def test_CustomUser_name(self):
        my_model = CustomUserFactory()
        self.assertEqual(f'{my_model.username}', str(my_model))

    def test_CustomUser_objects_get_query_set(self):
        for i in range(1, 11):
            if i % 2 == 0:
                CustomUserFactory(banned=True)
            else:
                CustomUserFactory(banned=False)

        my_query_set = CustomUser.objects.all()
        print(my_query_set)
        for object in my_query_set:
            self.assertEqual(object.banned, False)

    def test_CustomUser_delete(self):
        my_model = CustomUserFactory()
        my_model.delete()
        queryset = CustomUser.banned_manager.first()
        self.assertEqual(my_model, queryset)

    def test_Post_name(self):
        my_model = PostFactory()
        self.assertEqual(f'{my_model.title}', str(my_model))

    def test_Comment_name(self):
        my_model = CommentFactory()
        self.assertEqual(f'{my_model.author}: {my_model.content} ({my_model.Post})', str(my_model))

    def test_Answer_name(self):
        my_model = AnswerFactory()
        self.assertEqual(f"{my_model.author}: {my_model.content} ({my_model.comment})", str(my_model))
