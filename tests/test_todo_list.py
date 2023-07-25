import pytest
from lib.todo_list import *


"""
Given a string with TODO# 
returns True
"""
def test_string_with_todo():
    test_text = "I want to check for #TODO"
    assert check_todo(test_text) == True


"""
Given a string without TODO#
returns False
"""
def test_string_without_todo():
    test_text = "Hello, world how we doing??"
    assert check_todo(test_text) == False

"""
Given string with lower case #todo
returns True
"""
def test_lowercase_todo():
    test_text = "So today we need #todo studying"
    assert check_todo(test_text) == True

"""
raises Exception when given None
"""
def test_for_none():
    with pytest.raises(Exception) as error:
        check_todo(None)
    assert str(error.value) == "Please enter string!"

"""
raises exception error when not given string
"""
def test_for_no_string():
    with pytest.raises(Exception) as error:
        check_todo(1245)
    assert str(error.value) == "Please enter string!"



"""
raises error when given empty string
"""
def test_for_empty_string():
    with pytest.raises(Exception) as error:
        check_todo("")
    assert str(error.value) == "Please enter string!"
