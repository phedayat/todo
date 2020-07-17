import todo_item

class TodoStore:

    def __init__(self):
        self.numItems = 0
        self.todoListFile = None
        self.todoList = []

    def getNumItems(self):
        return self.numItems

    def addItem(self, todoItem):
        self.todoList.append(todoItem)
        self.numItems += 1
    
    def completeItem(self, numItem):
        self.todoList[int(numItem)].setCompleted(True)

    def exportList(self):
        self.todoListFile = open("todo_list.txt", "w")

        for item in self.todoList:
            item.itemToString()

        self.todoListFile.close()