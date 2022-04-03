import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('500x250')

frame = Frame(root)
frame.grid()

toolbar=root.title('Check Files')
toolbar.pack()
browse_btn1 = Button(root, text = 'Browse', width = 14)
browse_btn1.place()
browse_btn1.grid()



browse_btn2 = Button(root, text = 'Browse', width = 14)
browse_btn2.grid()

check_btn = Button(root, text = 'Check Files', width = 14, height=2)
check_btn.grid()

close_btn = Button(root, text = 'Close', width=14, height=2)
close_btn.pack()

browse_entry = Entry(root,width = 28)
browse_entry.place(height=700, width=100)
browse_entry.pack()



browse_entry2 = Entry(root,width = 28)
browse_entry2.pack()




root.mainloop()
