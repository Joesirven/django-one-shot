from django.urls import path
from todos.views import todos_list_list, todo_list_details

urlpatterns = [
    path(
        "",
        todos_list_list,
        name="todos_list_list",
    ),
    path(
        "<int:id>",
        todo_list_details,
        name="todo_list_details",
    ),
]
