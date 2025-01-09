import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2
print(x)
print(y)

#Basic Matplotlib Commands
plt.plot(x, y) # 'r' is the color red
plt.xlabel('X Axis Title')
plt.ylabel('Y Axis Title')
plt.title('String Title')
# plt.show()

#Use plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,2,2)
plt.plot(x, y, 'r--') #check color options if needed
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-')
plt.show()



