from matplotlib import pyplot as plt    

fig = plt.figure()
plt.plot(1,2,3)
fig.suptitle('test title', fontsize=20)
plt.xlabel('xlabel', fontsize=18)
plt.ylabel('ylabel', fontsize=16)
#fig.savefig('test.jpg')
plt.show()