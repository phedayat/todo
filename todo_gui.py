from tkinter import *
import todo_item
import todo_store

class Todo_Gui(Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.i = IntVar()
        self.priority = Entry(self.master, textvariable=self.i)
        self.priority.pack(side="top")

        self.hi = Button(self)
        self.hi["text"] = "Click here!"
        self.hi["command"] = self.add_item
        self.hi.pack(side="top")

        self.quit = Button(self, text="EXIT", fg="blue", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_item(self):
        item = TodoItem()


root = Tk()
app = Todo_Gui(master=root)
app.mainloop()