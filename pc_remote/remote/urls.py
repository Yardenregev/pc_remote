from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keypress/', views.keypress, name='keypress'),
    path('input/', views.input, name='input'),
    path('move_mouse/', views.move_mouse, name='move_mouse'),
    
]
