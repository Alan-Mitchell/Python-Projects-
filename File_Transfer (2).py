#importing all the needed modules 
import tkinter
from tkinter import *  
from tkinter import filedialog as fd
import os
import datetime as dt
import shutil
#function to source
def getSource():
    mydir = fd.askdirectory()
    srcdir.delete(0,END)
    srcdir.insert(0,mydir)
#function to destination
def getDestinatiom():
    newdir = fd.askdirectory()
    newloc.delete(0,END)
    newloc.insert(0,newdir)
#functon for file transfer
def file_transfer():
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    strftime = "%H:%M %m/%d/%Y"
    created =srcdir.get()
    dest = newloc.get()
    files= os.listdir(created)
    for fname in files:
        path = os.path.join(created, fname)
        st = os.path.getmtime(path)   
        mtime = dt.datetime.fromtimestamp(st)
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

