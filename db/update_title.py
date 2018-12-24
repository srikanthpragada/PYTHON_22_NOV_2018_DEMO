import sqlite3
con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
cur = con.cursor()

id =  input("Enter job id : ")

try:
    cur.execute("select title from jobs where id = ?", (id,))
    job = cur.fetchone()
    if job is None:
        print("Sorry! Job not found!")
    else:
        print("Job Title : ", job[0])  # display title
        title = input("Enter job title : ")
        cur.execute("update jobs set title = ? where id = ?", (title,id))
        if cur.rowcount == 1:
            print("Successfully updated job title!")
            con.commit()
        else:
            print("Sorry! Could not update job!")

except Exception as ex:
    print("Sorry! Some error -->", ex)


con.close()