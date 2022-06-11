from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    # Первый роут на главную страницу
    path('', views.index),
    # Роут на страницу записей
    path('users/', views.users),
    path("roles/", views.roles),
]
