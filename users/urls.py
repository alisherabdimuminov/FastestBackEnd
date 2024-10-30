from django.urls import path

from .views import (
    UsersListAPIView,

    add_user,

    edit_user,
)


urlpatterns = [
    path("", UsersListAPIView.as_view(), name="users"),
    path("add/", add_user, name="add_user"),
    path("<int:pk>/edit/", edit_user, name="edit_user"),
]
