"""
7. Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
Sample filename : abc.java
Output : java
"""
filename=input("Enter filename: ")

f_ext=filename.split(".")
print(f_ext)
print("Extension is",f_ext[-3])