#from data import students
#from database import *
import sqlite3
conn = sqlite3.connect("student.db")
#print("database connected successfully")
cursor=conn.cursor()
def insert():
    name= input("enter student name ")
    roll=int(input("please enter student roll number"))
    age= int(input("enter student age "))
    dob =(input("enter student date of birth "))
    mobile=int(input("enter student mobile no. "))
    address= input("enter student address ")
    
    cursor.execute(""" INSERT INTO students(name,roll,age,dob,mobile,address) 
                   VALUES(?,?,?,?,?,?)""",(name,roll,age,dob,mobile,address))
    conn.commit()
    print("fffff")
if __name__ == "__main__":
    insert()
    conn.close()