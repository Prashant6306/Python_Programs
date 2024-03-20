# # Program to check if a number is prime or not


#take a input from user
num=int(input("Enter the number:"))

flag=False

if num==1:
    print(num,"is not a prime number")
elif num>2:
    #check for factors
    for i in range(2,num):
        if num%i==0:
            flag=True
            break

    #check if flag is true
    if flag:
        print(num,"is not a prime number")
    else:
        print(num,"is a prime number")




















