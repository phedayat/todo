from tkinter import * # GUI
from todo_item import TodoItem # Class for a single TODO item
from todo_store import TodoStore # Class for containing all TODO items

class Todo_Gui(Frame):

    def __init__(self, master = None):
        '''
        Create a TODO GUI
        '''

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.store = TodoStore()

    def create_widgets(self):
        '''
        Create the widgets shown on screen.
        '''

        # Quit button
        quitter = Button(self.master, text="EXIT", fg="red", command=self.master.destroy)
        quitter.pack(side="right")

        # Add button
        add = Button(self.master, text="Add", command=self.add_item)
        add.pack(side="right")

        # Description textarea
        self.description = Text(self.master)
        self.description.pack(side="top")

        # Priority textfield
        self.priority = Entry(self.master, textvariable=IntVar())
        self.priority.pack(side="top")

        # Due checkbox
        self.due = StringVar()
        isDue = Checkbutton(self.master, text="Is it Due?", onvalue="true", offvalue="false", variable=self.due)
        isDue.pack(side="left")

        # Completed checkbox
        self.completed = StringVar()
        completedWidget = Checkbutton(self.master, text="Completed?", onvalue="true", offvalue="false", variable=self.completed)
        completedWidget.pack(side="left")

        # Print button
        printer = Button(self.master, text="Print", command=self.print_items)
        printer.pack(side="right")

        # Export button
        exporter = Button(self.master, text="Export", command=self.export)
        exporter.pack(side="right")

    def add_item(self):
        '''
        Add an item to the TODO store
        '''

        # print(self.priority.get())
        # print(self.due.get())
        # print(self.description.get("1.0", END))
        print(self.completed.get())
        item = TodoItem(self.description.get("1.0", END), self.completed.get(), self.priority.get(), self.due.get())
        self.store.addItem(item)

        displayBox = Checkbutton(self.master, text=item.itemToString(), onvalue="complete", offvalue="incomplete")
        displayBox.pack(side="bottom")

    def print_items(self):
        '''
        Print the TODO items to the screen
        '''

        listString = ""

        for item in self.store.todoList:
            listString += item.itemToString() + "\n"
        
        displayLabel = Label(self.master, text=listString)
        displayLabel.pack(side="bottom")

    def export(self):
        '''
        Export the TODO items to a text file
        '''

        self.store.exportList()

if __name__ == "__main__":
    root = Tk()
    app = Todo_Gui(master=root)
    app.mainloop()