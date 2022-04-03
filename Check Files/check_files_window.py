#Python Version 3.5.1
#
#Author: Alan Mitchell
#
#Purpose: Check Files program
#
#
#Tested OS: This code was written and tested to work with windows 10

#Imported needed modules
from tkinter import *
import tkinter as tk

#modules to created to run Check Files program
import check_files_GUI
import check_files_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define our master fram configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        #this CenterWindow method will center our app on the user's screen
        check_files_func.center_window(self,500,300)
        self.master.title('Check Files')
        self.master.configure(bg='FOFOFO')
        #this protocol method is a built-in method to catch if
        #the user clicks the upper corner X on Windows.
        self.master.protocol('WM_DELETE_WINDOW',lambda: check_files_func.ask_quit(self))
        arg=self.master

        #load in the GUI widget from a seperate module
        #keeping your code compartmetalized and clutter free.


if __name__ == '__main__':
    root= tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
