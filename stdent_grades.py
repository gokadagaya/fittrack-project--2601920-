# Tuple – subject names
subjects = ("Math", "Science", "English")

# List – student names
students = ["Raj", "Priya", "Amit", "Sneha", "Karan"]

# Dictionary – marks of each student
marks = {
    "Raj":    {"Math": 85, "Science": 78, "English": 90},
    "Priya":  {"Math": 92, "Science": 88, "English": 85},
    "Amit":   {"Math": 70, "Science": 75, "English": 68},
    "Sneha":  {"Math": 95, "Science": 90, "English": 92},
    "Karan":  {"Math": 80, "Science": 82, "English": 78}
}

# Set – to store unique grades
unique_grades = set()

print("All Students:", students)
print("First 3 Students:", students[:3])
print()

top_student = ""
highest_avg = 0

# Calculate average, grade, and find topper
for student in students:
    total = 0
    for subject in subjects:
        total += marks[student][subject]
    
    average = total / len(subjects)

    if average >= 85:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "C"

    unique_grades.add(grade)

    print(f"{student} - Average: {average:.2f} - Grade: {grade}")

    if average > highest_avg:
        highest_avg = average
        top_student = student

print()
print("Top Student:", top_student)
print("Unique Grades:", unique_grades)
