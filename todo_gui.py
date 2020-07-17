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
        self.isDue = Checkbutton(self.master, text="Is it Due?", onvalue="true", offvalue="false", variable=self.due)
        self.isDue.pack(side="bottom")

        self.hi = Button(self)
        self.hi["text"] = "Click here!"
        self.hi["command"] = self.add_item
        self.hi.pack(side="top")

        self.quit = Button(self, text="EXIT", fg="blue", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_item(self):
        print(self.priority.get())
        print(self.due.get())
        print(self.description.get("1.0", END))
        item = TodoItem(self.description.get(), self.completed.get(), self.priority.get(), self.isDue.get())
        self.store.addItem(item)

    def printItems(self):
        for item in self.store.todoList:
            print(item.)


if __name__ == "__main__":
    root = Tk()
    app = Todo_Gui(master=root)
    app.mainloop()