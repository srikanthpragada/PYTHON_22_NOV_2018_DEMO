import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
cur = con.cursor()

cur.execute("select count(*), avg(minsal), avg(maxsal) from jobs")

job_count,avg_minsal, avg_maxsal = cur.fetchone()
print("Count of jobs  : ", job_count);
print("Avg Min Salary : ", avg_minsal);
print("Avg Max Salary : ", avg_maxsal);
con.close()
