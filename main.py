from data import students
from insert import *
from view import *
from search import *
from update import *
from delete import *
from exit import *
print("******Studnent Record management*******")
print("1 add student")
print("2 View Students")
print("3 Search Student")
print("4 Update Student")
print("5 Delete Studen")
print("6 Exit")
while True:
    choice = int(input("enter your choice 1 to 6 ->"   ))
    if choice == 1:
        insert()
    elif choice == 2:
        View()
    elif choice == 3:
        search()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    elif choice == 6:
        exit()
        break
    else:
         print("invalid choice please try again")
   