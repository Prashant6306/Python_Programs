"""
Q.10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""
n=5
n1=int("%s"%n)
n2=int("%s%s"%(n,n))
n3=int("%s%s%s"%(n,n,n))
#n3=nnn

print(n1+n2+n3)