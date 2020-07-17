from tkinter import *
from todo_item import TodoItem # Class for a single TODO item
from todo_store import TodoStore # Class for containing all TODO items

class Todo_Gui(Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.priority = Entry(self.master)
        self.priority.pack(side="top")

        self.hi = Button(self)
        self.hi["text"] = "Click here!"
        self.hi["command"] = self.add_item
        self.hi.pack(side="top")

        self.quit = Button(self, text="EXIT", fg="blue", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_item(self):
        print(self.priority.get())


root = Tk()
app = Todo_Gui(master=root)
app.mainloop()