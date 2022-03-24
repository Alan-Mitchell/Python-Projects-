#importing the needed modules
import os
import webbrowser
from tkinter import *
#variable to create html file
htmlPage= open('Summer.html','w')
# variable for HTML contents
message='''

<html>
    <head></head>
        <body>
        <h1>Stay tuned for our amazing summer sale!</h1>
        </body>
</html>
'''
#methods used to control HTML file 
htmlPage.write(message)
htmlPage.close()
webbrowser.open_new_tab('Summer.html')

tkinter.simpledialog.askstring(title, prompt, **kw)
