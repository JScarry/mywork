#messing with histograme
#Author: Jarlath Scarry

import numpy as np
import matplotlib.pyplot as plt
'''
np.random.seed(1)
normData = np.random.normal(size=10)

plt.hist(normData)

plt.show()
'''
fruit = np.array(['Apples', 'Oranges','Banana'])
numbers = np.array([25,55,222])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()


