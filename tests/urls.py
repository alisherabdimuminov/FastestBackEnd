from django.urls import path

from .views import (
    QuestionListAPIView,
    SpecsListAPIView,
    TestsListAPIView,

    add_question,
    add_spec,
    add_test,

    edit_question,
    edit_spec,
    edit_test,
)


urlpatterns = [
    path("questions/", QuestionListAPIView.as_view(), name="questions"),
    path("specs/", SpecsListAPIView.as_view(), name="specs"),
    path("tests/", TestsListAPIView.as_view(), name="tests"),
    
    path("questions/add/", add_question, name="add_question"),
    path("specs/add/", add_spec, name="add_spec"),
    path("tests/add/", add_test, name="add_test"),

    path("questions/<int:pk>/edit/", edit_question, name="edit_test"),
    path("specs/<int:pk>/edit/", edit_spec, name="edit_test"),
    path("tests/<int:pk>/edit/", edit_test, name="edit_test"),
]
