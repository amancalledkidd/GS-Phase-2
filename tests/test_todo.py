from lib.todo import Todo

"""
Check Todo was initialised
assert task (str)
"""

def test_check_task():
    get_done = Todo('Workout')
    assert get_done.task =='Workout'

"""
test mark complete
returns True
"""

def test_mark_complete():
    get_done = Todo('Workout')
    get_done.mark_complete()
    assert get_done.complete == True