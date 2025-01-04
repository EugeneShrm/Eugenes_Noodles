from random import sample
import matplotlib.pyplot as plt
import numpy as np

#v1
data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()

#v2
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# rectangular box plot
plt.boxplot(data,vert=True,patch_artist=True); 
plt.show() 

#v3
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.scatter(x,y)
plt.show() 