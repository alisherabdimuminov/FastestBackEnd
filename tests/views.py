from datetime import datetime, timezone
import random

from django.http import HttpRequest
from rest_framework import generics
from rest_framework import decorators
from rest_framework import permissions
from rest_framework.response import Response

from .models import Question, Set, Test
from .serializers import (
    TestsModelSerializer, 
    QuestionModelSerializer, 
    SetModelSerializer,
    CreateTestModelSerializer,
    CreateQuestionModelSerializer,
    CreateSetModelSerializer,
    TestModelSerializer,
)

# LIST

class TestsListAPIView(generics.ListAPIView):
    queryset = Test.objects.all().order_by("-id")
    serializer_class = TestsModelSerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all().order_by("-id")
    serializer_class = QuestionModelSerializer


class SetsListAPIView(generics.ListAPIView):
    queryset = Set.objects.all().order_by("-id")
    serializer_class = SetModelSerializer


# ADD

@decorators.api_view(http_method_names=["POST"])
def add_test(request: HttpRequest):
    test = CreateTestModelSerializer(data=request.data)
    print(request.data)
    if test.is_valid():
        print(test.validated_data)
        test.create(test.validated_data)
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    print(test.errors)
    return Response({
        "status": "error",
        "code": "400",
        "data": None
    })


@decorators.api_view(http_method_names=["POST"])
def add_question(request: HttpRequest):
    question = CreateQuestionModelSerializer(data=request.data)
    print(request.data)
    if question.is_valid():
        question.create(question.validated_data)
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    print(question.errors)
    return Response({
        "status": "error",
        "code": "400",
        "data": None
    })


@decorators.api_view(http_method_names=["POST"])
def add_set(request: HttpRequest):
    Set = CreateSetModelSerializer(data=request.data)
    if Set.is_valid():
        Set.create(Set.validated_data)
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    return Response({
        "status": "error",
        "code": "400",
        "data": None
    })

# EDIT

def edit_test(request: HttpRequest, pk: int):
    test_obj = Test.objects.get(pk=pk)
    test = CreateTestModelSerializer(test_obj, data=request.data)
    if test.is_valid():
        test.create(test.validated_data)
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    return Response({
        "status": "error",
        "code": "400",
        "data": None
    })

@decorators.api_view(http_method_names=["POST"])
def edit_question(request: HttpRequest, pk: int):
    question_obj = Question.objects.get(pk=pk)
    question = CreateQuestionModelSerializer(question_obj, data=request.data)
    if question.is_valid():
        question.create(question.validated_data)
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    return Response({
        "status": "error",
        "code": "400",
        "data": None
    })

@decorators.api_view(http_method_names=["POST"])
def edit_set(request: HttpRequest, pk: int):
    Set_obj = Set.objects.get(pk=pk)
    Set = CreateSetModelSerializer(Set_obj, data=request.data)
    if Set.is_valid():
        Set.create(Set.validated_data)
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    return Response({
        "status": "error",
        "code": "400",
        "data": None
    })

@decorators.api_view(http_method_names=["GET"])
@decorators.permission_classes(permission_classes=[permissions.IsAuthenticated])
def tests_me(request: HttpRequest):
    user = request.user
    tests_obj = Test.objects.filter(user__pk=user.pk)
    tests = TestsModelSerializer(tests_obj, many=True)
    return Response(tests.data)


@decorators.api_view(http_method_names=["GET"])
@decorators.permission_classes(permission_classes=[permissions.IsAuthenticated])
def test(request: HttpRequest, uuid: str):
    test_obj = Test.objects.filter(uuid=uuid)
    if not test_obj:
        return Response({
            "status": "error",
            "code": "404",
            "data": None
        })
    test_obj = test_obj.first()
    test = TestModelSerializer(test_obj, many=False)
    return Response(test.data)


@decorators.api_view(http_method_names=["POST"])
@decorators.permission_classes(permission_classes=[permissions.IsAuthenticated])
def set_test_set_time(request: HttpRequest, uuid: str):
    test_obj = Test.objects.filter(uuid=uuid)
    start_time = request.data.get("start_time")
    if not test_obj:
        return Response({
            "status": "error",
            "code": "404",
            "data": None
        })
    test_obj = test_obj.first()
    if not test_obj.start_time:
        test_obj.start_time = start_time
        test_obj.save()
    return Response({
        "status": "success",
        "code": "200",
        "data": None
    })


@decorators.api_view(http_method_names=["POST"])
def submit(request: HttpRequest, uuid: str):
    now = datetime.now()
    test_obj = Test.objects.filter(uuid=uuid)
    if not test_obj:
        return Response({
            "status": "error",
            "code": "404",
            "data": None
        })
    test_obj = test_obj.first()
    questions = test_obj.questions.all()
    answer_keys = request.data.get("answers")
    cases = {}
    counter = 1
    percentage = 0
    for question, answer in zip(questions, answer_keys.split(",")):
        if answer == question.correct_answer:
            cases[f"{counter}"] = {
                "correct": question.correct_answer,
                "answer": answer,
                "status": True
            }
            percentage += question.score
        else:
            cases[f"{counter}"] = cases[f"{counter}"] = {
                "correct": question.correct_answer,
                "answer": answer,
                "status": False
            }
        counter+= 1
    print(percentage)
    print(test_obj.passed_score, percentage)
    if (test_obj.passed_score <= percentage):
        test_obj.status = "passed"
        test_obj.save()
    else:
        test_obj.status = "failed"
    if (test_obj.start_time):
        print(now.replace(tzinfo=timezone.utc), test_obj.start_time.timetz().tzinfo)
    test_obj.percentage = percentage
    test_obj.cases = cases
    test_obj.save()
    return Response({
        "status": "success",
        "code": "200",
        "data": None
    })


@decorators.api_view(http_method_names=["POST"])
def bulk_create(request: HttpRequest):
    raw_questions = request.data.get("raw")
    for raw_q in raw_questions.split("\n\n"):
        q = raw_q.split("\n")
        content = q[0]
        a = q[1]
        b = q[2]
        c = q[3]
        d = q[4]
        answers = {
            "a": a,
            "b": b,
            "c": c,
            "d": d,
        }
        items = list(answers.items())
        random.shuffle(items)
        shuffled_answers = dict(items)
        print(shuffled_answers)
        set = Set.objects.first()
        question = Question.objects.create(
            question=content,
            set=set
        )
        ans_counter = 0
        akeys = "abcd"
        for ans in shuffled_answers:
            if ans == "a":
                question.correct_answer = akeys[ans_counter] 
            ans_counter += 1
        question.answer_a = list(shuffled_answers.values())[0]
        question.answer_b = list(shuffled_answers.values())[1]
        question.answer_c = list(shuffled_answers.values())[2]
        question.answer_d = list(shuffled_answers.values())[3]
        question.save()
    return Response()
