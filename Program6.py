"""
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers. Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
values=input("Enter the comma seperated numbers: ")
print(values)
#print(type(values))
list1=values.split(" ")
print(list1)

tuple1=tuple(list1)
print(tuple1)