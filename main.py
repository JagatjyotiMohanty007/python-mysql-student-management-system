from crud import *

while True:

    print("\n===== Student Management System =====")
    print("1. Insert")
    print("2. View")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        city = input("City: ")

        insert_student(name, age, city)

    elif choice == "2":
        view_students()

    elif choice == "3":
        sid = int(input("Student ID: "))
        city = input("New City: ")

        update_student(sid, city)

    elif choice == "4":
        sid = int(input("Student ID: "))
        delete_student(sid)

    elif choice == "5":
        break
