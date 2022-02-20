#while loop practice
#author: Jarlath

count = 0
while count <= 9:
    print (count)
    count +=1
    
count = 10
while count >= 0:
   print (count)
   count -= 1
   

print ("Blast off")

val = input ("enter something (q to quit)")
while val != "q":
    print ("you said: " + val)
    val = input ("(q to quit):")
print ("Goodbye")

