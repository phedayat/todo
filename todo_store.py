import todo_item

class TodoStore:

    def __init__(self):
        self.numItems = 0
        self.todoListFile = None
        self.todoList = []

    def addItem(self, todoItem):
        self.todoList.append(todoItem)
    
    def completeItem(self, numItem):
        self.todoList[numItem].getCompleted()

    def exportList(self):
        self.todoListFile = open("todoList.txt", "w")

        for item in self.todoList:
            self.todoListFile.write(f"{item.getPriority()}: {item.getDescription()}; Due: {(item.isDue, item.due)[item.isDue]}")
        
        self.todoListFile.close()