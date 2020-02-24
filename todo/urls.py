from django.urls import path, include
from . import views


app_name = 'todo'


urlpatterns = [

    path('', views.todoView, name='todoView'),
    path('addtodo/', views.addTodo, name='addTodo'),
    path('deletetodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),
]
