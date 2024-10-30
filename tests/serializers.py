from rest_framework import serializers

from users.serializer import UserModelSerializer
from users.models import User

from .models import Test, Set, Question


class SetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ("id", "name", )


class CreateSetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ("name", )

class QuestionModelSerializer(serializers.ModelSerializer):
    set = SetModelSerializer(Set)
    class Meta:
        model = Question
        fields = ("question", "answer_a", "answer_b", "answer_c", "answer_d", "correct_answer", "score", "set", )

class CreateQuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("spec", "question", "answer_a", "answer_b", "answer_c", "answer_d", "correct_answer", "score", )


class TestModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(User, many=False)
    set = SetModelSerializer(Set)
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = Test
        fields = ("name", "user", "set", "start_time", "duration", "passed_score", "status", "percentage", "elapsed", )


class CreateTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ("name", "user", "set", "start_time", "duration", "passed_score", )
