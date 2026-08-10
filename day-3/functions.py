# Day 3: Functions in Python

# Simple function
def greet():
    print("Hello, welcome to Python!")


greet()


# Function with a parameter
def greet_user(name):
    print("Hello,", name)


greet_user("John")


# Function with two parameters
def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


# Function to calculate average
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


values = [10, 20, 30, 40, 50]

average = calculate_average(values)

print("Average:", average)


# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print("Number 15 is:", check_even_odd(15))
