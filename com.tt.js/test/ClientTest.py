__author__ = 'spatil'

#code for client test application goes here.

# Python asdasd program to check if the input number is prime or not asdsdasd

num = 240

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:

   # asdd check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not  prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is  prime number")

# adsasdsad if input number is less than or equal to 1, it is not prime

else: #sadada
   print(num,"is   not  prime number")