import math

number = int(input("Please Enter your number: "))
x = [1,2,3,4,5,6,7,8,9]
num = number - 1

for i in x:
    if number % i != 0:
        test = pow(i, num)

if (test % number is 1):
    print(number, " is a prime number")
else:
    print(number, " is not a prime number")