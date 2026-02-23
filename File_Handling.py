
#TASK 1: CREATE AND WRITE STUDENT DATA
#CODE:
# Task 1: Create and write student data
file = open("students.txt", "w")
file.write("Alice,85\n")
file.write("Bob,92\n")
file.write("Charlie,78\n")
file.write("Diana,95\n")
file.close()
print("students.txt file created and data written successfully.")
#EXPECTED OUTPUT:
#students.txt file created and data written successfully.
'''
EXPLANATION:
I used 'w' mode to create or overwrite the file. Each student record was written on a new
line using newline characters. Finally, I closed the file properly to ensure resources are
released.
TASK 2: READ AND DISPLAY DATA
CODE:
# Task 2: Read and display student data
*/'''
try:
 with open("students.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
   name, score = line.strip().split(",")
   print(f"Student: {name}, Score: {score}")
except FileNotFoundError:
 print("Error: students.txt file not found.")
#EXPECTED OUTPUT:
'''Student: Alice, Score: 85
Student: Bob, Score: 92
Student: Charlie, Score: 78
Student: Diana, Score: 95
EXPLANATION:
I used a 'with' block for safe file handling so the file closes automatically. The program reads
all lines, splits each record using a comma, and prints formatted output. I also handled
FileNotFoundError to prevent crashes.
TASK 3: APPEND NEW STUDENT AND CREATE LOG
CODE:
# Task 3: Append new student and create log
# Append new student
'''
with open("students.txt", "a") as file:
 file.write("Eve,88\n")
# Create log file
with open("activity.log", "w") as log_file:
 log_file.write("Added new student: Eve\n")
print("New student added and activity logged successfully.")

with open("activity.log", "r") as log:
   content=log.read()
   print(content)

with open("students.txt", "r") as student_file:
   str=student_file.read()
   print(str)


'''EXPECTED OUTPUT:
New student added and activity logged successfully.
EXPLANATION:
I used append mode ('a') to add a new student without deleting existing data. Then I created
a separate log file to record the action. Using 'with' ensures proper and safe file handling. 
'''