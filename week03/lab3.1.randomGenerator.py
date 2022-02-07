# program that prints out a random number
#Author: Jarlath


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

import random
number = random.randint(x,y) 
print("{} is a random number between {} and {}".format(number,x,y))
#prints out random number between x and y, but y must be bigger than x, otherwise get an error