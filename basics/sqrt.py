

num = int(input("enter a number (0 to Quit)")) #input the number

def sqroot(number):   #defining thefunction sqroot 
    return number ** 0.5 #calculation = number to the power of 0.5
if num != 0:
    print ("The square root of",num,"is", sqroot(num)) #print out the result
else:
    print("Quit")

