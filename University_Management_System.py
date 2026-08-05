# University Management System

university = {
    "CS101": {
        "course_name": "Computer Science",
        "students": ["John", "Mary", "David"]
    },
    "CS102": {
        "course_name": "Data Science",
        "students": ["Sophia", "Alex"]
    }
}

while True:
    print("\n===== UNIVERSITY MANAGEMENT =====")
    print("1. View Courses")
    print("2. View Students")
    print("3. Add Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nCourses")

        for course, details in university.items():
            print(course, "-", details["course_name"])

    elif choice == "2":
        course = input("Enter course code: ")

        if course in university:
            print("\nStudents")

            for student in university[course]["students"]:
                print(student)
        else:
            print("Course not found.")

    elif choice == "3":
        course = input("Enter course code: ")

        if course in university:
            student = input("Enter student name: ")
            university[course]["students"].append(student)
            print("Student added.")
        else:
            print("Course not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")