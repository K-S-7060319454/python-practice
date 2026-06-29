from data import students
def delete():
    search_roll=int(input("enter student roll no."))
    for student in students:
        if student[1] == search_roll:
            #print("yes student is present" , student)
            #student[0]=input("enter student new name")
            #student[2]=int(input("enter student new Age."))
            #print("successfully updated",student)
            students.remove(student)
            break
        print("Delete Student successfully")