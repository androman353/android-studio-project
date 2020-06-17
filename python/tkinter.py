from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter Your Name: ")

def myclick():
	myLabel = label(root, text=hello)
	myabel.pack()

myButton = Button(root, text="Enter your quote", command=myclick)
myButton.pack()


root. mainloop()
