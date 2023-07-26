import pytest
from lib.todo_class import *

"""
Initally, we have an empty todo list
"""
def test_init_empty_todo():
    todo_list = ToDoList() 
    assert todo_list.list() == []


"""
When we add a todo
The list updates
"""
def test_add_todo():
    todo_list = ToDoList()
    todo_list.add('Workout')
    assert todo_list.list() == ['Workout']

"""
When we complete a todo
It gets removed from the list
"""

def test_complete_todo():
    todo_list = ToDoList()
    todo_list.add('Workout')
    todo_list.add('Run')
    todo_list.add('Make smoothie')
    todo_list.complete('Run')
    assert todo_list.list() == ['Workout', 'Make smoothie']