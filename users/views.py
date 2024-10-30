from django.http import HttpRequest
from rest_framework import decorators
from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializer import UserModelSerializer



class UsersListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


@decorators.api_view(http_method_names=["POST"])
def add_user(request: HttpRequest):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone = request.data.get("phone")
    password = request.data.get("password")
    role = request.data.get("role")
    try:
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            pwd=password,
            role=role
        )
        user.set_password(password)
        user.save()
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    except:
        return Response({
            "status": "error",
            "code": "400",
            "data": None
        })

@decorators.api_view(http_method_names=["POST"])
def edit_user(request: HttpRequest, pk: int):
    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    phone = request.data.get("phone")
    password = request.data.get("password")
    role = request.data.get("role")
    user = User.objects.get(pk=pk)
    try:
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.pwd = password
        user.role = role
        user.set_password(password)
        user.save()
        return Response({
            "status": "success",
            "code": "201",
            "data": None
        })
    except:
        return Response({
            "status": "error",
            "code": "400",
            "data": None
        })
