from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models as m


# Create your models here.

class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(banned=False)


class CustomUser(AbstractUser, CustomUserManager):
    avatar = m.ImageField(
        blank=True,
        null=True,
    )
    banned = m.BooleanField(default=False)
    objects = CustomUserManager()

    def delete(self, *args, **kwargs):
        self.banned = True


class Category(m.Model):
    name = m.CharField(unique=True, blank=False, null=False, max_length=100)
    description = m.TextField(unique=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Post(m.Model):
    title = m.CharField(blank=False, null=False, max_length=100)
    content = m.TextField()
    photo = m.ImageField(blank=False, null=False)
    author = m.ForeignKey(CustomUser, on_delete=m.DO_NOTHING)
    download = m.IntegerField(default=0)
    date = m.DateTimeField(auto_now_add=True)
    categories = m.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.title


class Comment(m.Model):
    content = m.TextField()
    Post = m.ForeignKey(Post, on_delete=m.CASCADE)
    author = m.ForeignKey(CustomUser, on_delete=m.DO_NOTHING)
    date = m.DateTimeField()

    def __str__(self) -> str:
        return f'{self.author}: {self.content}'


class Answer(m.Model):
    content = m.TextField()
    comment = m.ForeignKey(Comment, on_delete=m.CASCADE)
    author = m.ForeignKey(CustomUser, on_delete=m.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.author}: {self.content}'