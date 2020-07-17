from tkinter import *
from todo_item import TodoItem # Class for a single TODO item
from todo_store import TodoStore # Class for containing all TODO items

class Todo_Gui(Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.store = TodoStore()

    def create_widgets(self):
        self.description = Text(self.master)
        self.description.pack(side="top")

        self.priority = Entry(self.master, textvariable=IntVar())
        self.priority.pack(side="top")

        self.due = StringVar()
        isDue = Checkbutton(self.master, text="Is it Due?", onvalue="true", offvalue="false", variable=self.due)
        isDue.pack(side="bottom")

        self.completed = StringVar()
        completedWidget = Checkbutton(self.master, text="Completed?", onvalue="true", offvalue="false", variable=self.completed)
        completedWidget.pack(side="bottom")

        printer = Button(self.master, text="Print", command=self.print_items)
        printer.pack(side="bottom")

        self.hi = Button(self)
        self.hi["text"] = "Click here!"
        self.hi["command"] = self.add_item
        self.hi.pack(side="top")

        self.quit = Button(self, text="EXIT", fg="blue", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_item(self):
        # print(self.priority.get())
        # print(self.due.get())
        # print(self.description.get("1.0", END))
        print(self.completed.get())
        item = TodoItem(self.description.get("1.0", END), self.completed.get(), self.priority.get(), self.due.get())
        self.store.addItem(item)

    def print_items(self):
        listString = ""

        for item in self.store.todoList:
            listString += item.itemToString()
        
        displayLabel = Label(self.master, text=listString)
        displayLabel.pack(side="bottom")


if __name__ == "__main__":
    root = Tk()
    app = Todo_Gui(master=root)
    app.mainloop()