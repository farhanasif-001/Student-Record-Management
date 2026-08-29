import json
UI = r"""===== STUDENT RECORD MANAGEMENT SYSTEM =====

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit"""

MENU_DETAILS = r"""
1. Name
2. Age
3. Course
4. Marks
"""


def get_name(prompt="\nWhat is the name of the student?: "):
    """Returns name"""

    while True:
        name = input(prompt).strip().title()
        
        if name:
            break

        print("Name can't be empty.")

    return name


def get_age(prompt="\nWhat is the age of the student?: "):
    """Returns age successfully in 'int' type"""

    while True:
        try: 
            age = int(input(prompt))

            if age <= 0:
                print("Age must be greater than 0.")
                continue
            elif age > 70:
                print("Please provide reasonable age!")
                continue

            break

        except ValueError:
            print("Please provide numerical value!")

    return age


def get_course(prompt="\nEnter the course name of the student: "):
    """Returns name"""

    while True:
        course = input(prompt).strip().title()

        if course:
            break

        print("Course can't be empty.")

    return course


def get_marks(prompt="\nWhat marks did the student get?: "):
    """Returns marks successfully in 'int' type"""

    while True:
        try:
            marks = int(input(prompt))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100!")
                continue

            break

        except ValueError:
            print("Please provide numerical value!")

    return marks


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
            user_input = int(input("\nEnter Your Choice. (1-6): "))
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
        print("students.json is successfully created\n")

    except json.JSONDecodeError:
        print("\nstudents.json is empty or contains invalid JSON.")

        students = []
        save_students(students_list= students)
        print("students.json has been successfully modified\n")
        
    return students


def create_student(student_id, name, age, course, marks):
    """Creates a student"""

    new_student = {
    "student_id": student_id,
    "name": name,
    "age": age,
    "course": course,
    "marks": marks
}
    return new_student


def add_student():
    '''Add new student to json file.'''

    students = load_students()

    name = get_name()                                                     # Name
    age = get_age()                                                       # Age of the Student
    course = get_course()                                            # Course
    marks = get_marks()                                                   # Marks

    if students:                                                          # Student ID
        # student_id = students[-1]["student_id"] + 1
        student_id = max(student["student_id"] for student in students) + 1

    else:
        student_id = 101

    new_student = create_student(student_id, name, age, course, marks)
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
    students = load_students()

    if not students:
        print("\nNo Student records found.\n")
        return

    while True:
        student_to_update = None

        try:
            student_id = int(input("\nEnter Student ID of the student to update the details: "))

            for student in students:
                if student_id == student["student_id"]:
                    student_to_update = student
                    print("\n===== CURRENT STUDENT DETAILS =====")
                    show_student_details(student_to_update)
                    break

            if student_to_update is None:
                print("\nStudent's record not found.\n")
                continue

            break

        except ValueError:
            print("\nPlease provide numerical value.\n")

    while True:
        try:
            what_to_update = int(input(f"{MENU_DETAILS}\nWhat do you want to update? Type(1-4)"))

            if 1 <= what_to_update <= 4:
                break

            else:
                print(f"\nPlease type an interger between 1 to 4{MENU_DETAILS}")

        except ValueError:
            print("\nPlease provide numerical value.\n")

    if what_to_update == 1:
        name = get_name(prompt="\nEnter the updated name: ")
        student_to_update["name"] = name
        print("\nName updated successfully.")

    elif what_to_update == 2:
        age = get_age("\nEnter the updated age: ")
        student_to_update["age"] = age
        print("\nAge updated successfully.")

    elif what_to_update == 3:
        course = get_course(prompt="\nEnter the updated course: ")
        student_to_update["course"] = course
        print("\nCourse updated successfully.")

    elif what_to_update == 4:
        marks = get_marks(prompt="\nEnter the updated marks: ")
        student_to_update["marks"] = marks
        print("\nMarks updated successfully.")

    save_students(students)


def delete_student():
    """Deletes the student's record from json file."""

    students = load_students()

    if not students:
        print("\nNo Student records found.\n")
        return

    while True:
        student_to_delete = None

        try:
            student_id = int(input(f"\nEnter the student id of the student whose records you wish to delete: "))
        except ValueError:
            print("\nPlease provide numerical value.\n")
            continue

        for student in students:
            if student_id == student["student_id"]:
                student_to_delete = student
                break

        if student_to_delete is None:
            print("\nStudent's record not found.\n")
            continue


        print("===== STUDENT TO DELETE =====")
        show_student_details(student_to_delete)

        break

    while True:
        deletion_confirmation = input("Are you sure you want to delete this student? (Y/N): ").strip().lower()

        if deletion_confirmation == 'y':
            students.remove(student_to_delete)

            print(f"\nStudent '{student_to_delete['name']}' deleted successfully.")

            save_students(students)
            break

        elif deletion_confirmation == 'n':
            print("\nStudent's record deletion aborted!")
            break

        else:
            print("\nPlease provide correct input. Type 'Y' or 'N'.")
            continue


def exit_program():
    print("Exiting Program...")

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
