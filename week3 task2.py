def mark_grade (x,y):
    if x > y:
        print ("Sorry, you did not achieve your target grade")

    elif x == y:
        print ("Congratulations, you've achieved your target grade")

    elif x < y:
        print ("Congratulations, you've achieved above your target grade")

   
student_A = int (input("enter target grade of student A: "))
examA = int (input ("enter exam results: "))

mark_grade (student_A, examA)

