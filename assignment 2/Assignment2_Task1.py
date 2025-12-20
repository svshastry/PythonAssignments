"""
Task 1:

Check if a Number is Even or Odd Problem Statement: Write a Python program that: 1. Takes an integer input from the user.
2. Checks whether the number is even or odd using an if-else statement.
3. Displays the result accordingly.

Expected Output:
The program should return an output like:
enter a number : 7
7 is an odd number
enter a number : 12
12 is an even number.
"""

num = int(input("enter a number : "))

# Check if the number is even or odd
# For even numbers, the remainder when divided by 2 is 0

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")
