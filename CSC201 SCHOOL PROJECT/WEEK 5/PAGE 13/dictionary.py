# Define a dictionary with some key-value pairs
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Accessing values in the dictionary
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("GPA:", student["gpa"])

# Modifying values in the dictionary
student["age"] = 21  # Update age
student["gpa"] = 3.9  # Update GPA

print("\nAfter modifications:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("GPA:", student["gpa"])

# Adding new key-value pairs
student["email"] = "johndoe@example.com"
student["phone"] = "123-456-7890"

print("\nAfter adding new key-value pairs:")
print("Email:", student["email"])
print("Phone:", student["phone"])

# Deleting a key-value pair
del student["phone"]

print("\nAfter deleting phone number:")
print("Student dictionary:", student)

# Looping through keys and values
print("\nLooping through keys and values:")
for key, value in student.items():
    print(key + ":", value)
