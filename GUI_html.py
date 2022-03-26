#import everything from tkinter
from tkinter import *

#Create window object
window=Tk()

#define text box
la=Label(window, text = 'Body')
la.grid(row=1,column=1)

#define entries
body_input=StringVar()
e=Entry(window,textvariable=body_input)
e.grid(row=0, column=1)


window.mainloop()


