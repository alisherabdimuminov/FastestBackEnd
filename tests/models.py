from django.db import models

from users.models import User


ANSWER = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
    ("d", "D"),
)
STATUS = (
    ("freeze", "Boshlanmagan"),
    ("passed", "O'tgan"),
    ("failed", "Yiqilgan"),
    ("ended", "Tugagan"),
)


class Spec(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    question = models.TextField()
    answer_a = models.TextField()
    answer_b = models.TextField()
    answer_c = models.TextField()
    answer_d = models.TextField()
    correct_answer = models.CharField(max_length=1, choices=ANSWER)
    score = models.IntegerField(default=1)

    def __str__(self):
        return self.question
    
class Test(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True, blank=True)
    score = models.CharField(max_length=100, null=True, blank=True)
    passed_score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
