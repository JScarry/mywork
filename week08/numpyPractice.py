
#https://stackoverflow.com/questions/67237632/attributeerror-partially-initialized-module-numpy1-has-no-attribute-array
#partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import)
#error de to .py file named numpy

import numpy as np
listOfnumbers = [4,3,2,1]
numbers = np.array([1,2,3,4])

#listOfnumbers = listOfnumbers + 3
numbers = numbers * np.array([1,4,5,6])


print (listOfnumbers)
print (numbers)

randomNumbers = np.random.randint(100, 200, 5)
normalNumbers = np.random.normal(100, 200, 5) 
print (randomNumbers)
print (normalNumbers)





