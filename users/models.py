from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


ROLE = (
    ("admin", "Admin"),
    ("user", "Xodim"),
    ("anonym", "XodimX"),
)
BRANCHES = (
    ("Asosiy", "Asosiy"),
    ("Pavarot", "Pavarot"),
    ("Mikrorayon", "Mikrorayon"),
)


class User(AbstractUser):
    uuid = models.CharField(max_length=100, default=uuid4)
    username = models.CharField(max_length=20, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=150)
    branch = models.CharField(max_length=100,null=True, blank=True, choices=BRANCHES, default="Давлат экологик экспертизаси маркази")
    department = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE)
    pwd = models.CharField(max_length=100, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self) -> str:
        return self.username
