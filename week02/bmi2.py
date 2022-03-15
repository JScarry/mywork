#Body mass index calculator
#Author: Jarlath Scarry

name = input ('Enter your name:')
print ('Hello {}\n Please answer the following questions and we\
    \n will calculate your Body Mass Index (BMI)'.format(name))
# \n to move code (and print out) onto next line

def readNum(message = "Enter your weight in KG:"): #defined function readNum, taken from week6 lectures
    num = False
    while (not num): #while loop continues until whole number in input
        try:
            num  = int(input(message))
        except ValueError:
            print ("Please enter whole numbers only. ", end="")
    return num    

num1 = readNum() # calls readNum and takes input as num1 (with default message)
num2 = readNum("Enter your height in cm:") # calls readNum and takes input as num2 (with message defined on this line)

bmi = num1 / (num2/100)**2 # calculation on the 2 numbers

print ('{} your weight is {}KG and height is {}CM.'.format(name, num1, num2))
print ('Your BMI is {:.2f}' .format(bmi)) #print out bmi to 2 decimal places

