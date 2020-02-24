from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    context = {'all_items': all_todo_items}
    return render(request, 'todo/todo.html', context)


def addTodo(request):
    # c = request.POST['content']
    # new_item = TodoItem(content = c)
    new_item = TodoItem(content = request.POST['content'])  # retriving data  and create a new item
    new_item.save()
    return  HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

