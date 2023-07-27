from lib.todo import Todo
from lib.todo_class import ToDoList

"""
When we add a todo
The list updates
"""
def test_add_todo():
    todo_list = ToDoList()
    workout = Todo('Workout')
    todo_list.add(workout)
    assert todo_list.incomplete() == [workout]

"""
returns a list of 
"""

# def test_complete_todo():
#     todo_list = ToDoList()
#     todo_list.add('Workout')
#     todo_list.add('Run')
#     todo_list.add('Make smoothie')
#     todo_list.complete('Run')
#     assert todo_list.list() == ['Workout', 'Make smoothie']