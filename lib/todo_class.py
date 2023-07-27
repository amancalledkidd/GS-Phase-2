class ToDoList():
    def __init__(self):
        self.incomplete_todo_list = []
        self.complete_todo_list = []

    def add(self, todo):
        self.incomplete_todo_list.append(todo)

    
    def incomplete(self):
        return self.incomplete_todo_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass