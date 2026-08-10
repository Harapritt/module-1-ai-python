# Day 3: Dictionaries in Python

# Creating a dictionary
student = {
    "name": "John",
    "age": 21,
    "course": "Computer Science",
    "marks": 85
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

# Adding a new key-value pair
student["city"] = "Kolkata"

print("\nUpdated student information:")
print(student)

# Looping through dictionary
print("\nStudent details:")

for key, value in student.items():
    print(key, ":", value)
