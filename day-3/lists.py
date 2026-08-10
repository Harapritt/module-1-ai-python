# Day 3: Lists in Python

# Creating a list
fruits = ["apple", "banana", "orange", "mango"]

print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Adding an element
fruits.append("grape")

print("After adding grape:", fruits)

# Removing an element
fruits.remove("banana")

print("After removing banana:", fruits)

# Looping through a list
print("\nAll fruits:")

for fruit in fruits:
    print(fruit)

# Finding the length of a list
print("\nNumber of fruits:", len(fruits))
