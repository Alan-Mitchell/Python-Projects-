import sqlite3

con = sqlite3.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_email TEXT)')
    con.commit()
con.close()

con = sqlite3.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute('INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('BOB','SMITH','BOB@GMAIL.COM'))
    cur.execute('INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('Jane','Jones','jj@aol.com'))
    cur.execute('INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('Alan','Mitchell','amithcell@aol.com'))
    
    cur.execute('INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES(?,?,?)'\
                ('Dan','Jobbs','alj@aol.com'))
    cur.execute('INSERT INTO tbl_persons(col_fname,col_lname,col_email) VALUES(?,?,?)',\
                ('vo','Tims','vt@GMAIL.COM'))
    con.commit()
con.close()    
    
    
