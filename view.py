from data import students
def View():
    if not students:
        print("record is empty")
    else:
        for student in students:
            print("Name         : ", student[0])
            print("Roll Number  : ", student[1])
            print("AGE          : ", student[2])
            print("DOB          : ", student[3])
            print("Mobile Number: ", student[4])
            print("Student Class: ", student[5])
            print("Address      : ", student[6])
            print("--------------------------------------")