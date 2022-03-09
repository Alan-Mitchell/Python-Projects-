import sqlite3
conn=sqlite3.connect('files.db')
with conn:
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        COL_FILENAME TEXT)')
    conn.commit()
conn.close()

fileList =('information.docx','Hello.txt','myImage.png',\
           'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
conn=sqlite3.connect('files.db')
with conn:
    for x in fileList:
        if x.endswith('.txt'):
        
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_files(COL_FILENAME)VALUES (?)',(x,))
            print(x)
            conn.commit()
conn.close()            
