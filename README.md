# Student Record Management System

A command-line student record management system built with Python. The application allows users to add, view, search, update, and delete student records, with data stored persistently in a JSON file.

## Features

- Add new student records
- View all student records
- Search students by:
  - Student ID
  - Name
  - Course
- Update student information
- Delete student records with confirmation
- Persistent JSON-based data storage
- Input validation
- Exception handling
- Automatic student ID generation

## Technologies Used

- Python
- JSON
- Git
- GitHub

## Project Structure

student-record-management/
├── main.py
├── students.json
└── README.md

## How to Run

### 1. Clone the repository

git clone https://github.com/farhanasif-001/student-record-management.git

### 2. Navigate to the project directory

cd student-record-management

### 3. Run the application

python main.py

## Data Storage

Student records are stored in `students.json`.

The application automatically loads existing records when it starts and saves changes to the JSON file when students are added, updated, or deleted.

## Input Validation

The application validates user input for:

- Empty names and course names
- Invalid numerical input
- Student age
- Student marks
- Menu selections
- Student IDs

## Future Improvements

- Add automated tests
- Add student statistics and reporting
- Add a graphical user interface
- Add PostgreSQL database support
- Build a REST API using FastAPI

## Author

**Farhan Asif**

[GitHub](https://github.com/farhanasif-001)