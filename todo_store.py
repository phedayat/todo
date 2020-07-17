import todo_item

class TodoStore:

    def __init__(self):
        self.numItems = 0
        self.todoList = []

    def getNumItems(self):
        return self.numItems

    def addItem(self, todoItem):
        self.todoList.append(todoItem)
        self.numItems += 1
    
    def completeItem(self, numItem):
        self.todoList[int(numItem)].setCompleted(True)

    def exportList(self):
        todoListFile = open("todo_list.txt", "w")

        for item in self.todoList:
            todoListFile.write(item.itemToString())

        todoListFile.close()