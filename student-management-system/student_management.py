class Student:

    roll_counter = 101

    def __init__(self, name, marks):
        self.roll_no = Student.roll_counter
        self.name = name
        self.marks = marks

        Student.roll_counter += 1

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            break
        except ValueError:
            print("\nChoose from the number (1-5) only...\n")

    if choice == 1:
        print("\n--- Enter Student Record ---")
        print("---------------------------------")
        while True:
            name = input("Enter student name: ").strip()
            if name:
                break
            print("\nName cannot be empty! Please enter a name.\n")
        while True:
            try:
                marks = float(input("Enter student marks: "))
                break
            except ValueError:
                print("\nInvalid marks! Enter a number.\n")
        print("---------------------------------")
        students.append(Student(name, marks))
        print(f"\nStudent added successfully!\nRoll No: {students[-1].roll_no}\n")

    elif choice == 2:
        if not students:
            print("No Record Found!")
        else:
            print("\n--- Student Records ---")
            print("-----------------------------------------")
            for student in students:
                student.display()
                print("-----------------------------------------")

            
    elif choice == 3:
        print("\n--- Search Student ---")
        print("---------------------------------")
        while True:
            try:
                roll_no = int(input("Enter roll number: "))
                break
            except ValueError:
                print("\nInvalid input! Please enter a numeric Roll No.\n")
        
        found = False
        for student in students:
            if student.roll_no == roll_no:
                print("\nStudent Found: ")
                print("---------------------------------")
                student.display()
                print("---------------------------------")
                found = True
                break  
        
        if not found:
            print("\nNo Record Found for roll number:", roll_no)

    elif choice == 4:
        print("\n--- Delete Student ---")
        print("---------------------------------")
        while True:
            try:
                roll_no = int(input("Enter roll number: "))
                break
            except ValueError:
                print("\nInvalid input! Please enter a numeric Roll No.\n")

        found = False
        for student in students:
            if student.roll_no == roll_no:
                students.remove(student)
                print(f"\nStudent with Roll No: {roll_no}, Name: {student.name}\nDeleted Successfully!")
                found = True
                break
            
        if not found:
            print("\nNo Student Found for roll number:", roll_no)

    elif choice == 5:
        print("\nExiting program...\n")
        break

    else:
        print("\nInvalid choice! Please select from 1 to 5.\n")
