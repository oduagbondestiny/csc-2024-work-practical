# Get user input for student's name and percentage grade
student_name = input("Enter student's name: ")
percentage_grade = float(input("Enter percentage grade: "))

# Determine the corresponding letter grade based on the cutoff points
if percentage_grade >= 90:
    letter_grade = 'A'
elif percentage_grade >= 80:
    letter_grade = 'B'
elif percentage_grade >= 70:
    letter_grade = 'C'
elif percentage_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display student's name, percentage grade, and corresponding letter grade
print("\nStudent's Name:", student_name)
print("Percentage Grade:", percentage_grade)
print("Letter Grade:", letter_grade)
