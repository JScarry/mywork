#OS module
#Author: Jarlath Scarry

import os

filename = 'test.txt'
if os.path.exists(filename):
    print(filename, 'exists')

else:
    print(filename, "not exist")
    