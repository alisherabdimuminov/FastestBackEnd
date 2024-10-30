from django.urls import path

from .views import (
    QuestionListAPIView,
    SetsListAPIView,
    TestsListAPIView,

    add_question,
    add_set,
    add_test,

    edit_question,
    edit_set,
    edit_test,
)


urlpatterns = [
    path("questions/", QuestionListAPIView.as_view(), name="questions"),
    path("sets/", SetsListAPIView.as_view(), name="sets"),
    path("tests/", TestsListAPIView.as_view(), name="tests"),
    
    path("questions/add/", add_question, name="add_question"),
    path("sets/add/", add_set, name="add_set"),
    path("tests/add/", add_test, name="add_test"),

    path("questions/<int:pk>/edit/", edit_question, name="edit_test"),
    path("sets/<int:pk>/edit/", edit_set, name="edit_set"),
    path("tests/<int:pk>/edit/", edit_test, name="edit_test"),
]
