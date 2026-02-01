student_name=input("Enter Student Name:")
maths_marks=int(input("Enter Maths Marks:"))
scinece_marks=int(input("Enter Scinece Marks:"))
english_marks=int(input("Enter English Marks:"))
is_valid=(maths_marks <0 or maths_marks > 100 )or(scinece_marks<0 or scinece_marks>100)or(english_marks <0 or english_marks>100)
if is_valid:
  print("Invalid marks entered")
else:
  total_marks=maths_marks+scinece_marks+english_marks
  percentage = (total_marks / 300) * 100
  if (maths_marks <40 or scinece_marks <40  or english_marks < 40):
     print("Student Name:",student_name)
     print(f"Total Marks: {total_marks}")
     print(f"Average Percentage: {percentage:.2f}%")
     print("Status : Fail")
  else:
    print("Student Name:",student_name)
    print(f"Total Marks: {total_marks}")
    print(f"Average Percentage: {percentage:.2f}%")
    print("Status : Pass")
    if(percentage>=75):
      print("Grade A")
    elif(percentage>=60 and percentage<75):
      print("Grade B")
    elif(percentage>=40 and percentage<60):
      print("Grade C")

