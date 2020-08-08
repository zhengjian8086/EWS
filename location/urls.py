from django.contrib import admin
from django.urls import path, include
from .views import Info

urlpatterns = [
    path('info', Info.as_view()),
]