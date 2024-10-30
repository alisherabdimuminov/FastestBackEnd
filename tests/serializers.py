from rest_framework import serializers

from users.serializer import UserModelSerializer
from users.models import User

from .models import Test, Spec, Question


class SpecModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spec
        fields = ("id", "name", )


class QuestionModelSerializer(serializers.ModelSerializer):
    spec = SpecModelSerializer(Spec)
    class Meta:
        model = Question
        fields = ("question", "answer_a", "answer_b", "answer_c", "answer_d", "correct_answer", "score", "spec", )

class TestModelSerializer(serializers.ModelSerializer):
    employee = UserModelSerializer(User, many=False)
    spec = SpecModelSerializer(Spec)
    class Meta:
        model = Test
        fields = ("name", "employee", "spec", "score", "passed_score", "status", )


class CreateTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("name", "employee", "spec", "status", "score", "passed_score", )


class CreateQuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("spec", "question", "answer_a", "answer_b", "answer_c", "answer_d", "correct_answer", "score", )


class CreateSpecModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spec
        fields = ("name", )
