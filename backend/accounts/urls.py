from django.contrib import admin
from django.urls import path
from .views import (
    StudentRegisterView,
    SuperUserRegisterView,
    StudentLoginView,
    SuperUserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path("student_register/", StudentRegisterView.as_view(), name="student_register"),
    path("superuser_register/", SuperUserRegisterView.as_view(), name="superuser_register"),
    path("student_login/", StudentLoginView.as_view(),name="student_login"),
    path("superuser_login/", SuperUserLoginView.as_view(),name="superuser_login"),
    path("logout/", UserLogoutView.as_view(),name="logout"),
]