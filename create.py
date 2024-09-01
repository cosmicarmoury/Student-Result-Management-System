import sqlite3
def create ():
    con=sqlite3.connect(database="project.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text, description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(rollno INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,course text,state text,city text,address text)")
    con.commit()
   
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks text,fmarks text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS user (eid INTEGER PRIMARY KEY AUTOINCREMENT,FName text,LName text, Email text,ContactNo text, Password text, CPassword text)")
    con.commit()
    con.close()


create()
    
