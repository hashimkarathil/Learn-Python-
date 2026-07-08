# add student
def add_student(students, name, marks):
    if name in students:
        print("Student already exists.")
    else:
        students[name] = marks
        print("Student added successfully!")

# calculate average
def calculate_average(marks):
    total = sum(marks)
    count = len(marks)
    return round(total / count, 2)

# display all students
def display_students(students):
    for name in students:
        marks = students[name]
        avg = calculate_average(marks)
        print("Name:", name, "| Marks:", marks, "| Average:", avg)

# find topper
def find_topper(students):
    highest_avg = 0
    topper_name = ""
    
    for name in students:
        marks = students[name]
        avg = calculate_average(marks)
        if avg > highest_avg:
            highest_avg = avg
            topper_name = name
            
    print("Topper:", topper_name, "(Average:", highest_avg, ")")

# menu
students = {}  

while True:
    print("\n--- Student Marks Analysis ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Find Topper")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        name = input("Enter student name: ")
        marks_string = input("Enter marks: ")
        
        
        marks_list = []
        for m in marks_string.split(","):
            marks_list.append(int(m))
            
        add_student(students, name, marks_list)
        
    elif choice == "2":
        display_students(students)
        
    elif choice == "3":
        find_topper(students)
        
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Plz try again.")