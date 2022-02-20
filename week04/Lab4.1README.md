Answers to Lab questions

Programming and Scripting
Lab Topic 04-Flow control if elif and else

Extra (I will not give the answer to these)
Q3. In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
equal to a Distinction.
How would you modify the program in 1 to deal with this?

Changed code to:
percentageRaw = float(input("Enter the percentage: "))
percentage = (round(percentageRaw))
print ("{} rounded is {}" .format(percentageRaw,percentage))

Q4. How would you use a while loop to modify 1 so that it keeps prompting the
user for a number until the user enters -1

percentageRaw = float(input("Enter the percentage (-1 to quit): (-1 to quit)"))
percentage = (round(percentageRaw))

if percentage == -1:
    print ('quit')
elif percentage < 0 or percentage > 100:
