#plot library
#based on matlab
#plot

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot(xpoints, xpoints, label="straight", color="blue")
plt.legend()

randomPoints = np.random.randint(1,10000,100)
plt.scatter(xpoints, randomPoints, label="random")
plt.legend()
plt.show()
#plt.savefig('week8-1.png')