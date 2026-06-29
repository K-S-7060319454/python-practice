from data import students
def search():
    search_name=input("enter user name")
    for student in students:
        if student[0] == search_name:
            print(student)   