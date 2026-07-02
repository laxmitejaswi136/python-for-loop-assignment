# ==========================================
# Python For Loop Assignment
# Author: Tejaswi Singu
# ==========================================

# Task 1: Sum of Squares of a List

print("Task 1: Sum of Squares")

numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total = total + (num ** 2)

print("Sum of Squares =", total)


# Task 2: Print Each Character of a String

print("\nTask 2: Print Each Character")

def print_characters(text):
    for ch in text:
        print(ch)

print_characters("Python")


# Task 3: Find the Maximum Number in a List

print("\nTask 3: Maximum Number")

numbers = [25, 10, 45, 18, 60, 32]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum Number =", maximum)


# Task 4: First 10 Fibonacci Numbers

print("\nTask 4: First 10 Fibonacci Numbers")

a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c


# Task 5: Print Dictionary Key-Value Pairs

print("\nTask 5: Dictionary Key-Value Pairs")

student = {
    "Name": "Tejaswi",
    "Age": 22,
    "Course": "Python"
}

for key, value in student.items():
    print(key, ":", value)

print("\nAssignment Completed Successfully!")