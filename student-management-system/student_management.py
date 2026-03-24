class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

students = []
while True:
    try:
        n = int(input("How many students would you like to enter: "))
        break
    except:
        print("\nInvalid input! Please enter a whole number.")
print("\n--- Enter Student Records ---\n")
for i in range(n):
    while True:
        try:
            name = input("Enter student name: ")
            marks = float(input("Enter student marks: "))
            print("-------------------------------------")
            students.append(Student(name, marks))
            break
        except:
            print("Invalid marks! Please enter a number (e.g., 85.5).\n")

print("\n--- Final Student Records ---\n")
for student in students:
    student.display()
    print("-------------------------------------")

if students:
    top_student = students[0]

    for student in students:
        if student.marks > top_student.marks:
            top_student = student

    print("\n--- Top Student ---")
    top_student.display()
else:
    print("No Record Found...")