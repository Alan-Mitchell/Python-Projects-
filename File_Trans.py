import tkinter as tk

root= tk.Tk()

canvas=tk.Canvas(root)
canvas.pack()

upload_entry=tk.Entry(root)
canvas.create_window(0,10,window=upload_entry)

source_entry=tk.Entry(root)
canvas.create_window(0,50,window=source_entry)

destin_entry=tk.Entry(root)
canvas.create_window(0,100,window=destin_entry)

uploadFile=tk.Button(root,text='Upload')
uploadFile.place(x=100,y=49)
uploadFile.pack()

source_loc=tk.Button(root,text='Source')
source_loc.place(x=100, y=0)
source_loc.pack()

destin_loc=tk.Button(root,text='Destination')
destin_loc.place(x=150,y=0)
destin_loc.pack()


root.mainloop()



