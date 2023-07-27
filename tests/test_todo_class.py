import pytest
from lib.todo_class import *

"""
Initally, we have an empty todo list
"""
def test_init_empty_todo():
    todo_list = ToDoList() 
    assert todo_list.incomplete() == []


