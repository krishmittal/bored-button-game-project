from tkinter import *
root=Tk()
def myClick():
    import loophighscore
myButton=Button(root,text="click me",command=myClick)
myButton.pack()
root.mainloop()
