#program to divide
#Author: Jarlath

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
#float accepts decimal place. entering other than number, eg hello gives an error.

answer = int(x//y) 
remainder = x%y

print (answer) #prints out answer with no detail
print ("answer is {} with remainder {} " .format (answer, remainder)) #prints out answer with remainder



print (" {} devided by {} is {} with remainder {} ".format (x, y, answer , remainder))
#prints answer in written format