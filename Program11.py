"""
Q:11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
Expected Result :
abs(number) -> number
Return the absolute value of the argument.
"""

import math
from math import sqrt
print(abs(-10.5))

print(sqrt.__doc__)
print("===============================")
print(help(sqrt))