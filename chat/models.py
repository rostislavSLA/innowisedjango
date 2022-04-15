from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Ticket(models.Model):
    STATUS = (
        ('open', 'open'),
        ('closed', 'closed')
    )
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    answer = models.TextField(default='')
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=7, choices=STATUS, default='open')
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ["-created"]


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

