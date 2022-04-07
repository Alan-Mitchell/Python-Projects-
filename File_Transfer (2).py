import tkinter
from tkinter import *  
from tkinter import filedialog as fd
from os import * as os
import datetime as dt
import shutil

def getSource():
    mydir = fd.askdirectory()
    srcdir.delete(0,END)
    srcdir.insert(0,mydir)

def getDestinatiom():
    newdir = fd.askdirectory()
    newloc.delete(0,END)
    newloc.insert(0,newdir)

def file_transfer():
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    strftime = "%H:%M %m/%d/%Y"
    created = \Users\Admin\Desktop\FolderA
    dest = C:\Users\Admin\Desktop\FolderB
    for m, in os.walk(created):  
    for fname in files:
        path = os.path.join(m, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dest)
            # this is actual move
    


m = tkinter.Tk() 

m.minsize(750,150)
m.title('Check Files')
btn_source = Button(m,width=12, text='SOURCE', padx=20, command=getSource)
btn_source.grid(row=2,column=0,padx=(25,0),pady=(45,10),sticky=W)

srcdir = Entry(m,text='')
srcdir.grid(row=2, column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

btn_destination = Button(m,width=12,text='DESTINATION',padx=20, command=getDestinatiom)
btn_destination.grid(row=3,column=0,padx=(15,0),pady=(45,10),sticky=W)

newloc = Entry(m,text='')
newloc.grid(row=3, column=1,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)


btn_checkFiles = Button(m,width=12, height=2, text='Check Files', padx=2, command=file_transfer)
btn_checkFiles.grid(row=4,column=0,padx=(15,0),pady=(45,10),sticky=W)



m.mainloop()  

