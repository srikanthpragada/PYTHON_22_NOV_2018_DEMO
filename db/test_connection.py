import sqlite3
con = sqlite3.connect(r"e:\classroom\python\nov22\hr.db")
print(type(con))
con.close()

