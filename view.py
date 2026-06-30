import sqlite3
from tabulate import tabulate
def View():
    conn= sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute("select* from students")
    records = cursor.fetchall()
    if not records:
        print("empty records")
    else:
        headers = ["ID","NAME","ROLL NUMBER","AGE","DOB","MOBILE NO.", "ADDRESS"]
        print(tabulate(records,headers=headers,tablefmt="grid"))
    """ if not records:
        print("empty records")
    else:
        for student in records:
            print(" ID ->" , student[0],
                  "name -> " , student[1], 
                  "roll number -> ", student[2],
                  "age -> ", student[3],
                  "DOB -> ", student[4],
                  "Mubile Number ->", student[5], 
                  "Address -> ", student[6])"""
    conn.close()
if __name__ == "__main__":
    View()
    
            
            
            
            
            
           