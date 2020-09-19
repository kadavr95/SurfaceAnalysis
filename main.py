import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

f = open("1.wft", "r")
hDim = int(f.readline())
vDim = int(f.readline())

a = np.zeros(shape=(hDim,vDim))
for x in range(hDim):
    for y in range(vDim):
        a[x,y] = float(f.readline())

plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()

ax = sns.heatmap(a)
plt.show()