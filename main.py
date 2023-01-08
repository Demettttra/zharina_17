import sqlite3

conn=sqlite3.connect('zharina.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS fio(id INTEGER PRIMARY KEY AUTOINCREMENT, column1  TEXT,
                column2 TEXT, column3 INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS animals(id INTEGER PRIMARY KEY AUTOINCREMENT, column1  TEXT,
                column2 INTEGER)''')
# cursor.execute('''INSERT INTO fio(column1,column2,column3) VALUES ('Aksana','Zharina','31')''')
# cursor.execute('''INSERT INTO fio(column1,column2,column3) VALUES ('Wasilisa','Vasilevskaya','31')''')
# cursor.execute('''INSERT INTO fio(column1,column2,column3) VALUES ('Alexei','Zharin','12')''')
cursor.execute('''INSERT INTO animals(column1,column2) VALUES ('cat','5')''')
cursor.execute('''INSERT INTO animals(column1,column2) VALUES ('dog','3')''')
cursor.execute('''INSERT INTO animals(column1,column2) VALUES ('pig','1')''')
conn.commit()