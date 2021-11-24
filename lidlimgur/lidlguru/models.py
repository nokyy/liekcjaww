from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models as m
from django.db.models import Manager


class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(banned=False)


class CustomUserManagerBanned(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(banned=True)


class CustomUser(AbstractUser, CustomUserManager):
    avatar = m.ImageField(
        blank=True,
        null=True,
    )
    banned = m.BooleanField(default=False)
    objects = CustomUserManager()
    banned_manager = CustomUserManagerBanned()
    normal_manager = UserManager()

    def delete(self, *args, **kwargs):
        self.banned = True
        self.save()


class Category(m.Model):
    name = m.CharField(unique=True, blank=False, null=False, max_length=100)
    description = m.TextField(unique=True, blank=False, null=False)

    objects = Manager

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

    objects = Manager

    def __str__(self) -> str:
        return self.title


class Comment(m.Model):
    content = m.TextField()
    Post = m.ForeignKey(Post, on_delete=m.CASCADE)
    author = m.ForeignKey(CustomUser, on_delete=m.DO_NOTHING)
    date = m.DateTimeField(auto_now_add=True)

    objects = Manager

    def __str__(self) -> str:
        return f"{self.author}: {self.content} ({self.Post})"


class Answer(m.Model):
    content = m.TextField()
    comment = m.ForeignKey(Comment, on_delete=m.CASCADE)
    author = m.ForeignKey(CustomUser, on_delete=m.DO_NOTHING)

    objects = Manager

    def __str__(self) -> str:
        return f"{self.author}: {self.content} ({self.comment})"
