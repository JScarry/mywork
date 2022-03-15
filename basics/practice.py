
num = int(input("enter a number "))
pwr = int(input("to the power of?:"))

def toPower(number, power=3):   #power if not set is 3, or below toPower(5 ,2) is to the power of 2
    print(number)
    print("to the power of", power)
    return number ** power


  
print (num,"to the power of",pwr,"is", toPower(num,pwr))
answer = toPower(5 , 2)
print (answer)
