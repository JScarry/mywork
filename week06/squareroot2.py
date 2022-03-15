#Algorithn to estimate square root
#Author: Jarlath Scarry

#Code from https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method


def newton_method(number, number_iters = 100):
    a = float(number) 
    for i in range(number_iters): 
        number = 0.5 * (number + a / number) 
    return number

a=int(input("Enter a number:"))


print("Square root of",a,"is:",newton_method(a))

#number - input("enter a number:")
#sqrt = square_root(number)
