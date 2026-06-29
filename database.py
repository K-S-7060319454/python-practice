import sqlite3
conn = sqlite3.connect("student.db")
#print("database connected successfully")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE If NOT EXISTS
               students(id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               roll INTEGER , 
               age INTEGER,
               dob TEXT,
               mobile TEXT, 
               address TEXT)""")
conn.commit()
print("student table create successfully")
conn.close()
