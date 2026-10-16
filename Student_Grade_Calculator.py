def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Congratulations!!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good! You can do even better!"
    elif marks >= 60:
        return "D", "Not bad but keep practicing!"
    else:
        return "F", "Don't give up! Study hard and try again!"

name = input("Enter student name: ").strip()

while not name:
    print("Invalid name! Please enter a student name.")
    name = input("Enter student name: ").strip()

while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks! Enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter numeric marks.")

grade, message = calculate_grade(marks)

print(f"\n📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks:g}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
