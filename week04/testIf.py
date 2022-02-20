#prog to show the format of an if statement
#Author: Jarlath

if True:
    print ("condition is true")

if 2 == 2:
    print ("yes it is!")

if 2 != 2:
    print ("wrong" )
else:
    print("2 not equal to 2 in false!")

x = 5
if (x % 2) == 0:  # I did not need the brackets, in for clarity
    print(x, " is even")  # another way of printing variables
elif (x % 3) == 0:  # if they number is even this will not be checked
    print(x, "is divisable by 3")
else:
    print(x, " is not even and is not divisable by 3")

print("this will always be outputted")

