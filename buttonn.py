from tkinter import *
root=Tk()
def myClick():
    import loop
myButton=Button(root,text="click me",command=myClick)
myButton.pack()
root.mainloop()
