  
import sqlite3
# first step is to always import the needed modules!
conn = sqlite3.connect('submission.db')
#conditional statment to access database and modify
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_example1(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_email TEXT)')
    conn.commit()
 


con = sqlite3.connect('submission.db')

with con:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_example1(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('Alan','Mitchell','am@aol.com'))
    cur.execute('INSERT INTO tbl_example1(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('John','Smith','js@aol.com'))
    cur.execute('INSERT INTO tbl_example1(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('Jane','Doe','jd@aol.com')) 
fileList =('information.docx','Hello.txt','myImage.png',\
           'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_example1(col_email)VALUES (?)'(x,))

   
conn.commit()
conn.close()







