from data import students
def update():
    search_roll=int(input("enter student roll no."))
    for student in students:
        if student[1] == search_roll:
            student[0]=input("enter student new name")
            student[2]=int(input("enter student new Age."))
            print("successfully updated",student)
            break
        else:
            print("record not found")