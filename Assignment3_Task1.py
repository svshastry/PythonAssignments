"""
Task 1: Calculate Factorial Using a Function
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument
and calculates its factorial using a loop or recursion.
2.   Factorial of a number, n! = n × (n−1) × (n−2) × ... × 1
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
Expected Output:
For example, if the function is called with 5, it should return:

Enter a number: 5
Factorial of 5 is : 120
"""

# Function to calculate factorial
def calculate_factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact = fact * i
    return fact

num = int(input("enter a number : "))

factorial = calculate_factorial(num)

print("Factorial of" ,num, "is :", factorial)
