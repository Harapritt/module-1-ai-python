# Day 3: Loops in Python

# 1. For loop
print("Numbers from 1 to 10:")

for i in range(1, 11):
    print(i)


# 2. Multiplication table
number = 5

print("\nMultiplication table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 3. While loop
print("\nWhile loop:")

count = 1

while count <= 5:
    print(count)
    count += 1


# 4. Sum of numbers from 1 to N
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print("\nSum of numbers from 1 to", n, ":", total)
