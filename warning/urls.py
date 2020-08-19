from django.contrib import admin
from django.urls import path, include
from .views import WarningInfo

urlpatterns = [
    path('info', WarningInfo.as_view()),
]
