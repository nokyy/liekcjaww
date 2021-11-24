import factory
import factory.fuzzy
from faker import Faker

fake = Faker()
from django.core.files.base import ContentFile
from lidlguru.models import Answer, Category, Comment, CustomUser, Post


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f'Username {n}')
    password = factory.PostGenerationMethodCall('set_password', 'Haslo123')
    banned = False
    avatar = None

    is_superuser = False
    is_staff = False
    is_active = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category{n}')
    description = factory.Sequence(lambda n: f'Description{n}')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: f'Title {n}')
    content = factory.Sequence(lambda n: f'Content {n}')
    photo = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'example.jpg'
        )
    )
    author = factory.SubFactory(CustomUserFactory)
    download = 0
    date = fake.date()

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.categories.add(group)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Sequence(lambda n: f'Comment {n}')
    Post = factory.SubFactory(PostFactory)
    author = factory.SubFactory(CustomUserFactory)
    date = fake.date()


class AnswerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Answer

    content = factory.Sequence(lambda n: f'Answer {n}')
    comment = factory.SubFactory(CommentFactory)
    author = factory.SubFactory(CustomUserFactory)
