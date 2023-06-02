from typing import Callable


def notebook() -> [Callable]:
    todo_list = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> [str]:
        return todo_list

    return add_todo, get_all


set_todo, get_todo = notebook()
for i in range(5):
    set_todo(f'Todo_{i}')

print(get_todo())
