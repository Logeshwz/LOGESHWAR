students = []
while True :
    print("\n=======SMART STUDENTS MANAGEMENT SYSTEM ============")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("ENTER YOUR CHOICE:"))

    if choice == 1:
        print("--------------------------------------------------------------------")

        print("Add students")
        student ={}
        
        student["ID"] = int(input("Enter Student ID:"))
        student["NAME"] = input("Enter Student Name:")
        student["AGE"] = int(input("Ener Your Age:"))
        student["DEPARTMENT"] = input("Enter Department:")
        student["MATHS"] = int(input("Enter Your Maths Mark:"))
        student["PHYSICS"] = int(input("Enter Your Physics Mark:"))
        student["CHEMISTRY"] = int(input("Enter Your Chemistry Mark:"))


        s1 = (student["MATHS"]+student["PHYSICS"]+student["CHEMISTRY"])
        student["total"] = s1
        print("TOTAL MARK", s1)

        a1 = s1/3
        student["average"] = a1
        print("AVERAGE MARK", a1)

        grade = a1
        student["grade"]=a1
        if a1>=90 and a1<=100:
            student["grade"] = "GRADE A+"
            print(student["grade"])

        elif a1>=80 and a1<=89:
            student["grade"] = "GRADE A"
            print(student["grade"])

        elif a1>=70 and a1<=79:
            student["grade"] = "GRADE B"
            print(student["grade"])

        elif a1>=60 and a1<=69:
            student["grade"] = "GRADE C"
            print(student["grade"])

        elif a1>=50 and a1<=59:
            student["grade"] = "GRADE D"
            print(student["grade"])

        elif a1<=49:
            student["grade"] = "GRADE F"
            print(student["grade"])

        students.append(student)
        print("\nstudent details successfully uploaded")
        print(student)

    elif choice == 2:
        print("View students")
     
        if len(students)==0:
            print("no students add in their page")

        else :
           for student in students :
               print("------------------------------------------------------------------")
               print("ID" , student["ID"])
               print("NAME" , student["NAME"])
               print("AGE" , student["AGE"])
               print("DEPARTMENT" , student["DEPARTMENT"])
               print("MATHS MARK" , student["MATHS"])
               print("PHYSICS" , student["PHYSICS"])
               print("CHEMISTRY" , student["CHEMISTRY"])
               print("TOTAL MARK" , student["total"])


    elif choice == 3:
        print("Search students")
        print("------------------------------------------------------------------")
        student_id =int(input("ENTER STUDENT ID:"))
        found = False
        for student in students :
            if student["ID"] == student_id :
                print("student is founded")
                print("ID" , student["ID"])
                print("NAME" , student["NAME"])
                print("AGE" , student["AGE"])
                print("DEPARTMENT" , student["DEPARTMENT"])
                print("MATHS MARK" , student["MATHS"])
                print("PHYSICS" , student["PHYSICS"])
                print("CHEMISTRY" , student["CHEMISTRY"])
                print("TOTAL MARK" , student["total"])
                found = True
                break
        found ==False
        print("student not founded")

    elif choice == 4:
        print("Update students")
        print("--------------------------------------------------------------------")
        update_id = int(input("ENTER STUDENT ID:"))
        found = False
        for student in students :
            if student["ID"] == update_id :
                print("STUDENT ID FOUNDED")
                student["NAME"] = input("ENTER CORRECT NAME:")
                student["AGE"] = int(input("ENTER CORRECT AGE :"))
                student["DEPARTMENT"] = input("ENTER CORRECT DEPARTMERNT:")
                student["MATHS"] = int(input("ENTER CORRECT MATHS MARK:"))
                student["PHYSICS"] = int(input("ENTER CORRECT PHYSICS MARK:"))
                student["CHEMISTRY"] = int(input("ENTER CORRECT CHEMISTRY MARK:"))

                a2 =(student["MATHS"]+student["PHYSICS"]+student["CHEMISTRY"])
                student["total"] = a2
                print("TOTAL MARK" , a2)
            
                s2 = a2/3
                student["AVERAGE"] = s2
                print("AVERAGE MARK", s2)

                grade = s2
                student["grade"]=s2
                if s2>=90 and s2<=100:
                    student["grade"] = "GRADE A+"
                    print(student["grade"])

                elif s2>=80 and s2<=89:
                    student["grade"] = "GRADE A"
                    print(student["grade"])

                elif s2>=70 and s2<=79:
                    student["grade"] = "GRADE B"
                    print(student["grade"])

                elif s2>=60 and s2<=69:
                    student["grade"] = "GRADE C"
                    print(student["grade"])

                elif s2>=50 and s2<=59:
                    student["grade"] = "GRADE D"
                    print(student["grade"])
 
                elif s2<=49:
                    student["grade"] = "GRADE F"
                    print(student["grade"])
   
                    found = True

                    print("student detail successfully updated")
                    print(student)

            else :
              print("NO STUDENT ID FOUNDED")

    elif choice == 5:
        print("Delete students")
        print("------------------------------------------------------------------------")
        delete_id = int(input("ENTER STUDENT ID:"))
        found = False
        for student in students :
            if student["ID"] == delete_id :
                print("STUDENT ID FOUNDED")
                students.remove(student)
                found = True
                print("STUDENT ID SUCCESSFULLY DELETED")
                break

            else :
                print("STUDENT ID NOT FOUNDED")


    elif choice == 6:
        print("Thanks For Choosing")
        break

    else:
        print("Invalid option")
