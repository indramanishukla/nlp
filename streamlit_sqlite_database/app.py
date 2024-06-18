import sqlite3
import pandas as pd

conn = sqlite3.connect('./streamlit_sqlite_database/data.db', check_same_thread=False)
cur = conn.cursor()

menu = [("paneer butter masala", 200), ("paneer lababdar", 220), ("dal makhni", 160)]

cur.execute("Create table if not exists menu(name text(50), price integer(30))")
cur.executemany("insert into menu values (?, ?)", menu)
conn.commit()
cur.close()


if __name__=='__main__':
    conn = sqlite3.connect('./streamlit_sqlite_database/data.db', check_same_thread=False)
    cur = conn.cursor()

    cur.execute("select * from menu")

    x = cur.fetchall()

    print(x)