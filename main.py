import time
import json
UI = r"""===== STUDENT RECORD MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit"""


def show_student_details(student):
    """Prints the detail of the student dictionary."""
    
    print("\n-------------------------")
    print(f"Student ID: {student['student_id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")
    print(f"Marks: {student['marks']}")
    print("-------------------------")


def get_choice():
    '''Get user input and return it.'''
    while True:
        try:
            user_input = int(input("Enter Your Choice. (1-6): "))
            return user_input
        except ValueError:
            print("Please Provide numerical inputs.\n")


def save_students(students_list):
    """Saves/Updates the student's data in the json file"""

    with open("./students.json", "w") as f:
        json.dump(students_list, f, indent=4)


def load_students():
    '''Load the students from json file if file exists otherwise creates a new json file.'''

    try:
        with open("./students.json", mode="r") as f:
            students = json.load(f)

    except FileNotFoundError:
        print("\nFile named 'students.json' not found.\nCreating a new json file...\n")

        students = []
        save_students(students_list= students)
        time.sleep(0.5)
        print("students.json is successfully created\n")

    except json.JSONDecodeError:
        print("\nstudents.json is empty or contains invalid JSON.")

        students = []
        save_students(students_list= students)
        time.sleep(0.5)
        print("students.json has been successfully modified\n")
        
    return students


def add_student():
    '''Add new student to json file.'''

    students = load_students()

    while True:                                                           # Name
        name = input("\nWhat is the name of the student?: ").strip().title()
        if name:
            break

        print("Name can't be empty.")

    while True:                                                           # Course
        course = input("\nEnter the course name of the student: ").strip().title()

        if course:
            break

        print("Course can't be empty.")

    if students:                                                          # Student ID
        # student_id = students[-1]["student_id"] + 1
        student_id = max(student["student_id"] for student in students) + 1

    else:
        student_id = 101

    while True:                                                           # Age of the Student
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
        "student_id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(new_student)

    save_students(students_list= students)

    print(f"\nStudent '{name}' added successfully.")


def view_students():
    students = load_students()

    if not students:
        print("\nNo student records found.\n")
        return

    print("\n===== ALL STUDENTS =====")

    for student in students:
        show_student_details(student)


def search_student():
    students = load_students()

    if not students:
        print("\nNo student records found.\n")
        return

    while True:
        search_by = input("How do you want to search ('student id', 'name', 'course')?: ").strip().lower()

        if search_by in ["student id", "name", "course"]:
            break

        print("Please choose among 'student id', 'name', 'course'.")

    # Search using student id
    if search_by == 'student id':
        while True:
            try:
                student_id = int(input(f"\nEnter the {search_by}: "))

                for student in students:
                    if student["student_id"] == student_id:
                        print(f"\n===== DETAILS OF THE STUDENT =====\n")
                        show_student_details(student)
                        return

                else:
                    print("\nStudent's record not found. Try again!\n")

            except ValueError:
                print("Please provide numerical inputs!")

    else:
        # Search using name and course
        while True:
            found = False
            field_name = input(f"\nEnter the Student's {search_by}: ").strip().title()

            for student in students:
                if student[search_by] == field_name:
                    show_student_details(student)
                    found = True


            if not found:
                print("\nStudent's record not found. Try again!\n")
            else:
                return
            


def update_student():
    print("Update Student feature coming soon")


def delete_student():
    print("Delete Student feature coming soon")


def exit_program():
    print("Exiting Program...")
    time.sleep(0.5)

menu_options = {
    1: add_student,
    2: view_students,
    3: search_student,
    4: update_student,
    5: delete_student,
}

while True:
    print("\n" * 4)
    print(UI)
    choice = get_choice()
    
    if choice in menu_options:
        menu_options[choice]()
    elif choice == 6:
        exit_program()
        break
    else:
        print("Please provide Valid input. (Valid inputs: 1, 2, 3, 4, 5, 6):\n")
