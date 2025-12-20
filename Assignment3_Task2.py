"""
Task 2: Using the Math Module for Calculations
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
Expected Output:
For example, if the user enters 25, the output should be:
Enter a number : 25
square root = 5.0
Logarithm = 3.2188758248682006
Sine = 0.13232142626552626

"""

import math

# Enter the number
num = float(input("Enter a number : "))

# Perform calculations using math module
square_root = math.sqrt(num)
log_value = math.log(num)
sine_value = math.sin(num)

# Display the results
print("square root =", square_root)
print("Logarithm =", log_value)
print("Sine =", sine_value)
