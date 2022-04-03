#imported the needed modules
from tkinter import *
import tkinter as tk

#modules to created to run Check Files program
import check_files_window
import check_files_func

def load_gui(self):
    self.btn_browse1 = tk.Button(self.master,width=12, text='Browse')
    self.btn_browse1.grid(row=2,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,text='Browse')
    self.btn_browse2.grid(row=3,column=0,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_checkFiles = tk.Button(self.master,width=12, height=2, text='Check Files')
    self.btn_checkFiles.grid(row=4,column=0,padx=(15,0),pady=(45,10),sticky=W)
    
    self.txt_browse1 = tk.Entry(self.master,text='')
    self.txt_browse1.grid(row=2, column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='')
    self.txt_browse2.grid(row=3, column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_checkFiles = tk.Entry(self.master,text='')
    self.txt_checkFiles.grid(row=4, column=2,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    
    


if __name__=='__main__':
    pass
