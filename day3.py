#Case study on Grade Calculator

# Student Details
student_name = input("Enter Student Name:")
student_id = input("Enter Student ID:")

#Marks Input
s1 = float(input("Enter Subject 1  Marks:"))
s2 = float(input("Enter Subject 2  Marks:"))
s3 = float(input("Enter Subject 3  Marks:"))
s4 = float(input("Enter Subject 4  Marks:"))
s5 = float(input("Enter Subject 5  Marks:"))

#Calculation
total = s1 + s2 + s2 + s4 + s5
percentage = total / 5

#Grade Logic
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade  = "C"
else:
    grade = "Fail"
    
# Output
print("\n--- Result ---")
print("Name:", student_name)
print("ID:",student_id)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
