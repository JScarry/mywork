#Algorithn to estimate square root
#Author: Jarlath Scarry

# Square Root of a Number using Newton's Method 
# | Python | 
# The Last Minute Professor
#https://www.youtube.com/watch?v=xdlIFw5EM4w

num = float(input("Enter a number:")) 
#read in input as a float

approx = 0.5*num 
#assume approx squareroot is half the input number

better = 0.5*(approx+num/approx)
#use the formula to calculate a better guess

while (better!=approx): 
    approx = better
    better=0.5*(approx+num/approx)
    #repeat the calculation until better is equal to approx

print("Squareroot",better) 
# print the result




