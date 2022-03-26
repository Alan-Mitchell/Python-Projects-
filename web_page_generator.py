#importing the needed modules
import os
import webbrowser
from tkinter import *

#create window object
window=Tk()

#define text box
la=Label(window, text = 'Body')
la.grid(row=1, column=1)

#define entries
body_input=StringVar()
e=Entry(window,textvariable=body_input)
e.grid(row=0,column=1)

def Submit():
    text=e.get()
    html_template = '''
    <html>
    <body>
    <h1>
    {}
    </h1>
    </body>
    </html>
    '''.format(text)
    f= open('Summer.html','w')
    print(html_template)
    #writing code into file
    f.write(html_template)
    f.close()
    webbrowser.open_new_tab('Summer.html')

#define buttons
b=Button(window,text = 'Submit',command = lambda:Submit())
b.grid(row=2, column=3)



window.mainloop()


