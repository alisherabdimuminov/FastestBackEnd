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
    ("Давлат экологик экспертизаси маркази", "Давлат экологик экспертизаси маркази"),
    ("Қорақалпоғистон Республикаси филиали", "Қорақалпоғистон Республикаси филиали"),
    ("Андижон вилояти филиали", "Андижон вилояти филиали"),
    ("Бухоро вилояти филиали", "Бухоро вилояти филиали"),
    ("Жиззах вилояти филиали", "Жиззах вилояти филиали"),
    ("Қашқадарё вилояти филиали", "Қашқадарё вилояти филиали"),
    ("Наманган вилояти филиали", "Наманган вилояти филиали"),
    ("Навоий вилояти филиали", "Навоий вилояти филиали"),
    ("Самарқанд вилояти филиали", "Самарқанд вилояти филиали"),
    ("Сурхондарё вилояти филиали", "Сурхондарё вилояти филиали"),
    ("Сирдарё вилояти филиали", "Сирдарё вилояти филиали"),
    ("Тошкент вилояти филиали", "Тошкент вилояти филиали"),
    ("Тошкент шаҳар филиали", "Тошкент шаҳар филиали"),
    ("Фарғона вилояти филиали", "Фарғона вилояти филиали"),
    ("Хоразм вилояти филиали", "Хоразм вилояти филиали"),
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
