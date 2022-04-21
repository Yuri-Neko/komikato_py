from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comic/<str:endpoint>/', views.comic, name='comic'),
    path('chapter/<str:endpoint>/', views.chapter, name='chapter'),
]