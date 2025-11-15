"""
    Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:
numeral format = int, float
"""

a = input("Enter your first number: ", )
b = input("Enter your second number: ", )
c = float(a) + float(b)
d = float(a) - float(b)
e = float(a) * float(b)
f = float(a) / float(b)
print("Addition ", "=", c)
print("Subtraction ", "=", d)
print("Multiplication ", "=", e)
print("Division ", "=", f)
