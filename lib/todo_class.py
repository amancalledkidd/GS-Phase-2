"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

"""

"""
Initally, we have an empty todo list
"""

# todo_list = ToDoList() 
# todo_list.list() # => []


"""
When we add a todo
The list updates
"""

# todo_list = ToDoList()
# todo_list.add('Workout')
# todo_list.list() # => ['Workout']

"""
When we complete a todo
It gets removed from the list
"""

# todo_list = ToDoList()
# todo_list.add('Workout')
# todo_list.add('Run')
# todo_list.add('Make smoothie')
# todo_list.complete('Run')
# todo_list.list() # => ['Workout', 'Make smoothie']


class ToDoList():
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        self.todo_list.append(todo)

    def complete(self, todo):
        if todo in self.todo_list:
            self.todo_list.remove(todo)

    def list(self):
        return self.todo_list