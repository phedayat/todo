class TodoItem:

    def __init__(self, description, completed = False, priority = 0, isDue = False):
        self.priority = priority
        self.description = description
        self.isDue = isDue
        self.completed = completed

        if self.isDue:
            self.due = ""

    def setDescription(self, newDesc):
        self.description = newDesc

    def setPriority(self, newPriority):
        if newPriority < 0 or newPriority > 3:
            print("Priority can only be 0-3")
        else:
            self.priority = newPriority
    
    def setIsDue(self, newBool, newDue = ""):
        if newBool and self.isDue:
            print(f"This TODO item is already due {self.due}")
        elif not newBool and self.isDue:
            self.due = ""
        elif newBool and not self.isDue:
            self.due = newDue
        else:
            print("This TODO item is already not due")
    
    def setCompleted(self, completion):
        self.completed = completion

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority
    
    def getIsDue(self):
        return self.isDue
    
    def getDue(self):
        if self.due == "":
            print("This TODO item is not due and has no due date")
        else:
            return self.due
    
    def getCompleted(self):
        return self.completed