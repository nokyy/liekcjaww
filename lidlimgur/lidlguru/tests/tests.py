import factory
from django.test import TestCase
from django.test import Client
from django.db.models import signals

from lidlguru.tests.factories.factories import CustomUserFactory, PostFactory


class TestsSerializers(TestCase):
    @classmethod
    def setUpClass(self):
        self.c = Client()
        self.user = CustomUserFactory(username='Kacper')
        for x in range(0,20):
            PostFactory()
    @classmethod
    def tearDownClass(cls):
        pass

    @factory.django.mute_signals(signals.post_save)
    def test_post_view(self):
        self.c.force_login(self.user, backend=None)
        response = self.c.get('/post/')
        print(response.data)
        assert False
