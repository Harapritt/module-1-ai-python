# Day 4: Beginner Python Programs

# 1. Check whether a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 2. Find the largest of three numbers

a = 10
b = 25
c = 15

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)


# 3. Calculate factorial of a number

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial of", number, ":", factorial)


# 4. Check whether a number is prime

number = 17
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")


# 5. Reverse a string

text = "Python"

reversed_text = text[::-1]

print("Original string:", text)
print("Reversed string:", reversed_text)


# 6. Count vowels in a string

text = "Artificial Intelligence"
vowels = "aeiouAEIOU"
count = 0

for character in text:
    if character in vowels:
        count += 1

print("Number of vowels:", count)


# 7. Calculate the average of numbers

numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

print("Average:", average)
