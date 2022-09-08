from tkinter import *


root = Tk()


#
# myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
#
#
# myLabel2 = Label(root, text = "Sthhh").grid(row = 10, column = 1)
#
# myLabel3 = Label(root, text = "kkkkkk").grid(row = 11, column = 2)




str = [("Name",0,0),("Age",0,1),("Gender",0,2)]


Label_List = [Label(root, text = label).grid(row = r, column = c) for label, r, c in str]




# myLabel1.pack()
# myLabel2.pack()
# myLabel3.pack()

root.mainloop()
