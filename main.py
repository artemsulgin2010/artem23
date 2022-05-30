import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    userid INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT);
 """)

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS orders(
    orderid INT PRIMARY KEY,
    date TEXT,
    userid TEXT,
    total TEXT);
""")

conn.commit()



cur.execute("""INSERT INTO users(userid, fname, lname, gender)
    VALUES('0001', 'Artem', 'Slais', 'Male');""")

conn.commit()

user = ('00002', 'Arab', 'kobla', 'Femele')

order = ('00011', 'drim', 'Rik', 'Male')

conn.commit()


cur.execute("""SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN  users ON users.userid=orders.userid;""")
print(cur.fetchall())
conn.commit()