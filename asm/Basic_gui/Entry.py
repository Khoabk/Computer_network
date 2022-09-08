from tkinter import *

root = Tk()

root.geometry("100x100")

e = Entry(root, width = 100, borderwidth = 20, bg = "white", fg = "blue")

e.pack()


e.insert(0, "Write sth")

def sth():
    Label(root, text = e.get()).pack()
    print(e.get())
    e.insert(10, "Write sth")


myButton = Button(root, text = "Click Me!",command = sth, fg = "green", bg = "cyan")

myButton.pack()











root.mainloop()
