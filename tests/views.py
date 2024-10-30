from django.http import HttpRequest
from rest_framework import generics
from rest_framework import decorators
from rest_framework.response import Response

from .models import Question, Spec, Test
from .serializers import (
    TestModelSerializer, 
    QuestionModelSerializer, 
    SpecModelSerializer,
    CreateTestModelSerializer,
    CreateQuestionModelSerializer,
    CreateSpecModelSerializer,
)

# LIST

class TestsListAPIView(generics.ListAPIView):
    queryset = Test.objects.all().order_by("-id")
    serializer_class = TestModelSerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all().order_by("-id")
    serializer_class = QuestionModelSerializer


class SpecsListAPIView(generics.ListAPIView):
    queryset = Spec.objects.all().order_by("-id")
    serializer_class = SpecModelSerializer


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
def add_spec(request: HttpRequest):
    spec = CreateSpecModelSerializer(data=request.data)
    if spec.is_valid():
        spec.create(spec.validated_data)
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
def edit_spec(request: HttpRequest, pk: int):
    spec_obj = Spec.objects.get(pk=pk)
    spec = CreateSpecModelSerializer(spec_obj, data=request.data)
    if spec.is_valid():
        spec.create(spec.validated_data)
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