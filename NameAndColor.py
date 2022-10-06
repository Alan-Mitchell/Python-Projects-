from tkinter import *
from PIL import ImageTk,Image
import sqlite3



root = Tk()
root.title('Name and Favorite Color')
root.geometry("400x400")

#Database

#Create a database or connect to one
conn = sqlite3.connect('Name_Color.db')

#Create Cursor
c = conn.cursor()

#Create Table

c.execute("""CREATE TABLE Guests(
        Name text,
        FavoriteColor text)
        

""")

#Create Submit function for database
def submit():
    #Create a database or connect to one
    conn = sqlite3.connect('Name_Color.db')

    #Create Cursor
    c = conn.cursor()

    #Insert Into Table
    c.execute("INSERT INTO Guests VALUES(:Name, :FavoriteColor)",
              
                {'Name': Name.get(),
                 'FavoriteColor':FavoriteColor.get()}
              )

    #Commit Changes
    conn.commit()

    #close connection
    conn.close()


    
    #clear text box
    Name.delete(0,END)
    FavoriteColor.delete(0,END)

#Create Query function
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('Name_Color.db')

    #Create Cursor
    c = conn.cursor()

    #query the database
    c.execute("SELECT *,oid FROM Guests")
    records=c.fetchall()
    #print(records)

    #Loop thru results
    print_records=''

    for record in records:
        print_records += str(record) + "\n"


    query_label = Label(root, text=print_records)
    query_label.grid(row=5, column=0, columnspan=2)
    
    #Commit Changes
    conn.commit()

    #close connection
    conn.close()

#Create Text box
Name = Entry(root, width=30)
Name.grid(row = 0, column =0, padx=20 )

FavoriteColor = Entry(root, width=30)
FavoriteColor.grid(row = 0, column =1, padx=20 )

#Create Text Box Labels
Name_Label = Label(root,text="Name")
Name_Label.grid(row=1,column=0)

FavoriteColor_Label = Label(root,text="FavoriteColor")
FavoriteColor_Label.grid(row=1,column=1)

# Create a Submit Button
submit_btn = Button(root, text = "Add Record", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text = "Show Records", command=query)
query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


#Commit Changes
conn.commit()

#close connection
conn.close()


root.mainloop()


