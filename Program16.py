"""
Q.16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

"""

def differ(n):
    if n<17:
        return (17-n)
    else:
        return (n-17)*2


res1=differ(22)
print(res1)
res2=differ(14)
print(res2)