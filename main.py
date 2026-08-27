import time
UI = r"""===== STUDENT RECORD MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit"""

def get_choice():
    while True:
        try:
            user_input = int(input("Enter Your Choice. (1-6): "))
            return user_input
        except ValueError:
            print("Please Provide numerical inputs.\n")


def add_student():
    print("Add Student feature coming soon")


def view_students():
    print("View Students feature coming soon")


def search_student():
    print("Search Student feature coming soon")


def update_student():
    print("Update Student feature coming soon")


def delete_student():
    print("Delete Student feature coming soon")


def exit_program():
    print("Exiting Program...")
    time.sleep(1)

field = {
    1 : add_student,
    2 : view_students,
    3 : search_student,
    4 : update_student,
    5 : delete_student,
}

while True:
    print(UI)
    choice = get_choice()
    
    if choice in field:
        field[choice]()
    elif choice == 6:
        exit_program()
        break
    else:
        print("Please provide Valid input. (Valid inputs: 1, 2, 3, 4, 5, 6):\n")
