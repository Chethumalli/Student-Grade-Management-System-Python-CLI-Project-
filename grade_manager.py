import os
import json

FILE_NAME = "students.json"

# Load existing data if available
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add a new student
def add_student(data):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []
    for subject in ["Maths", "Science", "English"]:
        score = float(input(f"Enter marks for {subject} (out of 100): "))
        marks.append(score)

    total = sum(marks)
    percentage = total / 3
    grade = calculate_grade(percentage)

    student = {
        "Name": name,
        "Roll No": roll,
        "Marks": marks,
        "Total": total,
        "Percentage": round(percentage, 2),
        "Grade": grade
    }
    data.append(student)
    save_data(data)
    print("✅ Student added successfully!")

# Calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "F"

# View all students
def view_students(data):
    if not data:
        print("No student records found!")
        return
    print("\n--- Student Records ---")
    for s in data:
        print(f"Name: {s['Name']} | Roll No: {s['Roll No']} | Total: {s['Total']} | %: {s['Percentage']} | Grade: {s['Grade']}")

# Main menu
def main():
    data = load_data()
    while True:
        print("\n===== Student Grade Management =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
