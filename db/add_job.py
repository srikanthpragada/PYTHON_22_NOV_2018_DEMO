import sqlite3
con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
cur = con.cursor()

title =  input("Enter job title : ")
minsal = input("Enter min salary: ")
maxsal = input("Enter max salary: ")

try:
    cur.execute("insert into jobs(title,minsal,maxsal) values(?,?,?)",
            (title,minsal,maxsal))
    if cur.rowcount == 1:
        con.commit()
        print("Job has been added successfully!")
except:
    print("Sorry! Could not add job!")


con.close()