import sqlite3

con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
cur = con.cursor()

cur.execute("select * from jobs")
for id, title, minsal, maxsal in cur.fetchall():
    print(f"{id:2d} {title:20s} {minsal:6d} {maxsal:6d}")

con.close()
