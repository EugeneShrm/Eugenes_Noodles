import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 11)
y = x ** 2

array = np.ones(5, 5)*10
array2 = array ** 2
print(array)
print(array2)

plt.plot(array, array2, "g") # 'r' is the color red
plt.xlabel('X Axis Title')
plt.ylabel('Y Axis Title')
plt.title('String Title')
plt.show()