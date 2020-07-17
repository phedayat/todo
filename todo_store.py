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

    def itemToString(self, item):
        if item.getCompleted():
            return f"[x] {item.getPriority()}: {item.getDescription()}; Due: {item.due if item.isDue == False else item.isDue}\n"
        else:
            return f"[ ] {item.getPriority()}: {item.getDescription()}; Due: {item.due if item.isDue == False else item.isDue}\n"

    def exportList(self):
        self.todoListFile = open("todoList.txt", "w")

        for item in self.todoList:
            self.itemToString(item)
            
        self.todoListFile.close()