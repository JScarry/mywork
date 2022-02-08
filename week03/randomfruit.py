#Program that prints out a random fruit from a list of fruits
#Author: Jarlath

import random  # without this line I got NameError: name 'random' is not defined

fruits = ['apple', 'orange', 'banana', 'pear'] #created a list of fruits

index = random.randint ( 0,len(fruits)-1) 
fruit = fruits[index]

print("A Random Fruit:{}".format(fruit))

# another solution maybe   13 print(random.choice(fruits))
