# 🎓 Student Grade Management System (Python CLI Project)

A simple and efficient **Student Grade Management System** developed using **Python**. This Command Line Interface (CLI) application allows users to manage student records, calculate grades, store academic information, and generate performance reports.

The project demonstrates core Python programming concepts such as file handling, functions, loops, conditional statements, and data structures.

---

## 🚀 Features

- 👨‍🎓 Add new student records
- 📝 Enter and update student marks
- 📊 Calculate grades automatically
- 📈 Generate student performance reports
- 🔍 Search student records
- ❌ Delete student information
- 💾 Store data using file handling
- 📋 View all student records
- ⚡ Easy-to-use CLI interface
- 🔒 Input validation and error handling

---

## 🛠️ Tech Stack

- **Language:** Python
- **Interface:** Command Line Interface (CLI)
- **Storage:** Text Files / CSV Files
- **IDE:** VS Code / PyCharm

---

## 📂 Project Structure

```bash
Student-Grade-Management-System/
│
├── main.py
├── student.py
├── grade_calculator.py
├── data/
│   └── students.csv
│
├── reports/
│   └── performance_report.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Chethumalli/Student-Grade-Management-System-Python-CLI-Project-.git
cd Student-Grade-Management-System-Python-CLI-Project-
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> If no external libraries are used, you can skip this step.

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📋 Menu Options

```text
===== Student Grade Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Calculate Grades
7. Generate Report
8. Exit
```

---

## 🎓 Grade Calculation Logic

| Percentage | Grade |
|------------|--------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

---

## 📊 Sample Student Record

```text
Student ID : 101
Name       : John Doe
Marks      : 87
Grade      : A
Status     : Pass
```

---

## 💾 Data Storage

Student information can be stored in:

```csv
StudentID,Name,Marks,Grade
101,John Doe,87,A
102,Alice,92,A+
103,Bob,75,B
```

This allows records to persist even after the application is closed.

---

## 🔍 Core Functionalities

### Add Student

```python
add_student()
```

Adds a new student record to the database.

### Search Student

```python
search_student(student_id)
```

Searches student details using Student ID.

### Update Marks

```python
update_marks(student_id, new_marks)
```

Updates student marks and recalculates grades.

### Delete Student

```python
delete_student(student_id)
```

Removes a student record from the system.

### Generate Report

```python
generate_report()
```

Creates a report containing student performance data.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Programming Fundamentals
- Functions and Modular Programming
- Conditional Statements
- Loops and Iteration
- Lists and Dictionaries
- File Handling
- Data Management
- CLI Application Development
- Error Handling and Validation

---

## 🌟 Future Enhancements

- GUI using Tkinter
- Database integration with SQLite/MySQL
- Student login system
- Attendance management
- Subject-wise grading
- PDF report generation
- Data visualization and analytics
- Web-based version using Flask or Django

---

## 📸 Sample Output

```text
=====================================
Student Grade Management System
=====================================

Student Added Successfully!

Student ID : 101
Name       : John Doe
Marks      : 87
Grade      : A
Status     : Pass
```

---

## 👨‍💻 Author

### Chethan C Malli

- GitHub: https://github.com/Chethumalli
- LinkedIn: https://www.linkedin.com/in/chethumalli

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, please give it a **Star ⭐** on GitHub and support the project!
