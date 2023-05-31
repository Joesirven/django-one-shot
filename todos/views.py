from django.shortcuts import render, get_list_or_404
from todos.models import TodoList, TodoItem

# Create your views here.


def todos_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todos_list": todos,
    }
    return render(request, "todos/list.html", context)
