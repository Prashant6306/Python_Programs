"""
4. Write a Python program that calculates the area of a circle based on the radius entered by the user. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
r=float(input("Enter the radius: "))
from math import pi
aoc=(pi*(r**2))
print("Area of circle is",aoc)