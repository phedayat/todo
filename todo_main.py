from todo_store import TodoStore
from todo_item import TodoItem

mainStore = TodoStore()

command = input("What would you like to do? ")

while command != "quit":
    if command == "add":
        priority = input("Priority: ")
        description = input("Description: ")
        isDue = input("Is it due (True/False): ")

        if isDue == True:
            due = input("Due date: ")
        
        item = TodoItem(description, priority=priority, isDue=isDue)
        mainStore.addItem(item)
    elif command == "complete":
        itemNum = input("Enter item number: ")

        mainStore.completeItem(itemNum)
    elif command == "export":
        mainStore.exportList()
    elif command == "total":
        print(f"Number of items: {mainStore.getNumItems()}")
    
    command = input("What would you like to do? ")

exit(0)