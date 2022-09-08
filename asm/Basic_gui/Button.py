from tkinter import *

root = Tk()


def sth():
    Label(root, text = "Hello world!!").pack()
    print("Button clicked")



myButton = Button(root, text = "Click Me!",command = sth, fg = "green", bg = "cyan")

myButton.pack()


root.mainloop()
