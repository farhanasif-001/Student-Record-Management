import time
import json
UI = r"""===== STUDENT RECORD MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit"""

def get_choice():
    '''get user input and returns it.'''
    while True:
        try:
            user_input = int(input("Enter Your Choice. (1-6): "))
            return user_input
        except ValueError:
            print("Please Provide numerical inputs.\n")


def load_students():
    '''Load the students from json file if file exists otherwise create new json file.'''

    try:
        with open("./students.json", mode="r") as f:
            data = json.load(f)

    except FileNotFoundError:
        print("\nFile named 'students.json' not found.\nCreating a new json file...\n")

        data = []

        with open("./students.json", mode="w") as f:
            json.dump(data,f)
            time.sleep(0.5)

        time.sleep(0.5)
        print("students.json is successfully created\n")

    except json.JSONDecodeError:
        print("\nstudents.json is empty or contains invalid JSON.")

        data = []

        with open("students.json", "w") as f:
            json.dump(data, f)

    return data


def add_student():
    '''Add new student to json file.'''

    students = load_students()

    while True:                                                       # Name
        name = input("\nWhat is the name of the student?: ").strip().title()
        if name:
            break

        print("Name can't be empty.")

    while True:                                                       # Course
        course = input("Enter the course name of the student: ").strip().title()

        if course:
            break

        print("Course can't be empty.")

    if students:                                                          # Student ID
        # student_id = students[-1]["student_id"] + 1
        student_id = max(student["student_id"] for student in students) + 1

    else:
        student_id = 101

    while True:                                                       # Age of the Student
        try: 
            age = int(input("\nWhat is the age of the student?: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue
            elif age > 70:
                print("Please provide reasonable age!")
                continue

            break

        except ValueError:
            print("Please provide numerical value!")

    while True:
        try:
            marks = int(input("\nWhat marks did the student get?: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100!")
                continue

            break

        except ValueError:
            print("Please provide numerical value!")

    new_student = {
        "student_id" : student_id,
        "name" : name,
        "age" : age,
        "course" : course,
        "marks" : marks
    }

    students.append(new_student)

    with open("./students.json", "w") as f:
        json.dump(students, f, indent=4)

    print(f"\n Student '{name}' added sucessfully.")


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
    time.sleep(0.5)

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
